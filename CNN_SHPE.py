import torch
import torch.nn as nn
import torch.optim.lr_scheduler as lrs
from torch.utils.data import DataLoader, Dataset, random_split
import torchvision
from torchvision import datasets
from torchvision import transforms
import matplotlib.pyplot as plt
from tqdm import tqdm
import pytesseract
from PIL import Image
import os
from pathlib import Path
import numpy as np
from tokenizers import Tokenizer
from tqdm.auto import tqdm
import torch.optim as optim
from torch.nn.utils.rnn import pad_sequence
from torch.nn import functional as F
import pandas as pd


class Network(nn.Module):
    def __init__(self, num_classes=10, dropout=0.3):
        super(Network, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 256, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )

        self.avgpool = nn.AdaptiveAvgPool2d((6, 6))
        self.classifier = nn.Sequential(
            nn.Dropout(p=dropout),
            nn.Linear(256 * 6 * 6, 512),
            nn.ReLU(inplace=True),
            nn.Dropout(p=dropout),
            nn.Linear(512, 512),
            nn.ReLU(inplace=True),
            nn.Linear(512, num_classes),
        )

    def forward(self, x):
        N, c, H, W = x.shape
        features = self.features(x)
        pooled_features = self.avgpool(features)
        output = self.classifier(torch.flatten(pooled_features, 1))
        return output


def train(train_loader, model, criterion, optimizer):
    model.train()
    loss_ = 0.0
    losses = []
    it_train = tqdm(
        enumerate(train_loader),
        total=len(train_loader),
        desc="Training ...",
        position=0,
    )  # progress bar
    for i, (images, labels) in it_train:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        losses.append(loss)
        it_train.set_description(f"loss: {loss:.3f}")
    return torch.stack(losses).mean().item()


def train_model(
    model, train_loader, val_loader, criterion, optimizer, num_epochs, device
):
    best_val_acc = 0.0
    train_losses = []
    val_losses = []
    train_accs = []
    val_accs = []

    for epoch in range(num_epochs):
        # Training phase
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for images, labels in tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs}"):
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        epoch_loss = running_loss / len(train_loader)
        epoch_acc = 100 * correct / total
        train_losses.append(epoch_loss)
        train_accs.append(epoch_acc)

        # Validation phase
        model.eval()
        val_loss = 0.0
        correct = 0
        total = 0

        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)

                val_loss += loss.item()
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        val_loss = val_loss / len(val_loader)
        val_acc = 100 * correct / total
        val_losses.append(val_loss)
        val_accs.append(val_acc)

        print(f"Epoch {epoch+1}/{num_epochs}:")
        print(f"Training Loss: {epoch_loss:.4f}, Training Accuracy: {epoch_acc:.2f}%")
        print(f"Validation Loss: {val_loss:.4f}, Validation Accuracy: {val_acc:.2f}%")

        # Save best model
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), "best_model.pth")

    return train_losses, train_accs, val_losses, val_accs


class LoteriaDataset(Dataset):
    def __init__(self, csv_file, img_dir, transform=None):
        self.data = pd.read_csv(csv_file)
        self.img_dir = img_dir
        self.transform = transform
        self.label_map = {
            label: idx for idx, label in enumerate(self.data["label"].unique())
        }

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_name = self.data.iloc[idx, 0]
        img_path = os.path.join(self.img_dir, img_name)
        image = Image.open(img_path).convert("RGB")
        label = self.data.iloc[idx, 1]
        label = self.label_map[label]

        ## to show the image
        # plt.imshow(image)
        # plt.axis('off')
        # plt.show()

        if self.transform:
            image = self.transform(image)
        label = torch.tensor(label)

        return image, label


if __name__ == "__main__":

    train_transform = transforms.Compose(
        [
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ColorJitter(
                brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1
            ),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    csv_file = "loteria_dataset/loteria.csv"
    img_dir = "loteria_dataset"

    train_set = LoteriaDataset(
        csv_file=csv_file, img_dir=img_dir, transform=train_transform
    )

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "mps" if torch.backends.mps.is_available() else "cpu"
    )
    print(f"Using device: {device}")

    num_classes = len(train_set.data["label"].unique())
    batch_size = 32

    train_size = int(0.8 * len(train_set))
    val_size = len(train_set) - train_size
    train_dataset, val_dataset = random_split(train_set, [train_size, val_size])

    train_loader = DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True, num_workers=2
    )
    val_loader = DataLoader(
        val_dataset, batch_size=batch_size, shuffle=False, num_workers=2
    )

    model = Network(num_classes=num_classes).to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.0001)
    lr_scheduler = lrs.StepLR(optimizer, step_size=5, gamma=0.1)
    criterion = nn.CrossEntropyLoss()

    num_epochs = 50
    train_losses, train_accs, val_losses, val_accs = train_model(
        model, train_loader, val_loader, criterion, optimizer, num_epochs, device
    )

    torch.save(
        {
            "batch_size": batch_size,
            "epoch": num_epochs,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "train_losses": train_losses,
            "val_losses": val_losses,
            "train_accs": train_accs,
            "val_accs": val_accs,
        },
        "final_model.pth",
    )
