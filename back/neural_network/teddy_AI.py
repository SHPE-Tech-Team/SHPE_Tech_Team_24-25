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
from torchvision.models import resnet50, ResNet50_Weights


class Network(nn.Module):
    def __init__(self, num_classes=54, dropout=0.5):
        super(Network, self).__init__()
        # ResNet50 for feature extractor
        # self.backbone = resnet50(pretrained=True)
        self.backbone = resnet50(weights=ResNet50_Weights.DEFAULT)
        self.backbone.fc = nn.Identity()

        self.classifier = nn.Sequential(
            nn.Dropout(p=dropout),
            nn.Linear(2048, 1024),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(1024),
            nn.Dropout(p=dropout),
            nn.Linear(1024, 512),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(512),
            nn.Linear(512, num_classes),
        )

    def forward(self, x):
        x = self.backbone(x)
        x = self.classifier(x)
        return x


def train_model(
    model, train_loader, val_loader, criterion, optimizer, num_epochs, device
):
    best_val_acc = 0.0
    train_losses = []
    val_losses = []
    train_accs = []
    val_accs = []
    for epoch in range(num_epochs):
        # training phase
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

        # validation phase
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

        # saving the best model
        # if val_acc > best_val_acc:
        #     best_val_acc = val_acc
        #     torch.save(
        #         {
        #             "batch_size": batch_size,
        #             "epoch": num_epochs,
        #             "model_state_dict": model.state_dict(),
        #             "optimizer_state_dict": optimizer.state_dict(),
        #             "train_losses": train_losses,
        #             "val_losses": val_losses,
        #             "train_accs": train_accs,
        #             "val_accs": val_accs,
        #         },
        #         "best_model.pth",
        #     )
    return train_losses, train_accs, val_losses, val_accs


# plot accuracy
def plot_accuracy(train, val, test_frequency, num_epochs):
    indices = [
        i
        for i in range(num_epochs)
        if ((i + 1) % test_frequency == 0 or i == 0 or i == 1)
    ]
    plt.plot(indices, train, label="train")
    plt.plot(indices, val, label="val")
    plt.title("Accuracy Plot")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend()
    plt.show(block=False)


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
            transforms.Resize((256, 256)),  # Resize larger then crop
            transforms.RandomCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(15),
            transforms.ColorJitter(
                brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1
            ),
            transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
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
    # device = torch.device("cpu")
    print(f"Using device: {device}")

    num_classes = len(train_set.data["label"].unique())
    batch_size = 32

    # shuffle
    train_loader = DataLoader(
        train_set,
        batch_size=batch_size,
        shuffle=True,
        num_workers=3,
    )
    # no shuffle
    val_loader = DataLoader(
        train_set,
        batch_size=batch_size,
        shuffle=False,
        num_workers=3,
    )

    model = Network(num_classes=num_classes).to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    lr_scheduler = lrs.StepLR(optimizer, step_size=10, gamma=0.5)
    criterion = nn.CrossEntropyLoss()

    num_epochs = 50
    train_losses, train_accs, val_losses, val_accs = train_model(
        model, train_loader, val_loader, criterion, optimizer, num_epochs, device
    )
    plot_accuracy(train_accs, val_accs, 1, num_epochs)

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
