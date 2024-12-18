import torch
import torch.nn as nn
import torch.optim.lr_scheduler as lrs
from torch.utils.data import DataLoader
import torchvision
from torchvision import datasets
from torchvision import transforms
import matplotlib.pyplot as plt
from tqdm import tqdm

import os
from pathlib import Path
import numpy as np


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


model = Network(num_classes=37)


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
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        losses.append(loss)
        it_train.set_description(f"loss: {loss:.3f}")
    return torch.stack(losses).mean().item()


def test(test_loader, model, criterion):
    model.eval()
    losses = []
    correct = 0
    total = 0
    it_test = tqdm(
        enumerate(test_loader),
        total=len(test_loader),
        desc="Validating ...",
        position=0,
    )
    for i, (images, labels) in it_test:
        output = model(images)  
        preds = torch.argmax(output, dim=-1)
        loss = criterion(output, labels)
        losses.append(loss.item())
        correct += (preds == labels).sum().item()
        total += len(labels)

    mean_accuracy = correct / total
    test_loss = np.mean(losses)
    print("Mean Accuracy: {0:.4f}".format(mean_accuracy))
    print("Avg loss: {}".format(test_loss))
    return mean_accuracy, test_loss


train_transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(degrees=15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)

test_transform = transforms.Compose(
    [
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)
