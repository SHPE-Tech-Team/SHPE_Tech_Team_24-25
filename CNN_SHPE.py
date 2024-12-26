import torch
import torch.nn as nn
import torch.optim.lr_scheduler as lrs
from torch.utils.data import DataLoader, Dataset
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
    def __init__(self, num_classes=10, dropout=0.5):
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
        print(f"Image type: {type(images)}, Label type: {type(labels)}")
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        losses.append(loss)
        it_train.set_description(f"loss: {loss:.3f}")
    return torch.stack(losses).mean().item()


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
            transforms.Resize(256),
            transforms.RandomCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(degrees=15),
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
    model = Network(num_classes=num_classes)
    model.to(device)
    batch_size = 32

    train_loader = DataLoader(
        train_set, batch_size=batch_size, shuffle=True, num_workers=1
    )

    optimizer = optim.Adam(model.parameters(), lr=0.001)
    lr_scheduler = lrs.StepLR(optimizer, step_size=5, gamma=0.1)
    criterion = nn.CrossEntropyLoss()

    # print(f"Dataset size: {len(train_set)}")
    # print(f"Sample image shape: {train_set[0][1].shape}")
    # print(f"Sample label: {train_set[0][1]}")

    # num_epochs = 20
    # for epoch in tqdm(
    #     range(num_epochs), total=num_epochs, desc="Training ...", position=1
    # ):
    #     train_loss = train(train_loader, model, criterion, optimizer)
