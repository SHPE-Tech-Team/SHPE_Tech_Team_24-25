import torch
import torch.nn as nn
import torch.optim.lr_scheduler as lrs
from torch.utils.data import DataLoader
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


def text_extract(image):
    return pytesseract.image_to_string(image)


class Dataset_SetUp(dataset):
    def __init__(self, image_dir, image_transform=None, text_tokenizer=None):
        self.image_dir = image_dir
        self.image_transform = image_transform
        self.text_tokenizer = text_tokenizer
        self.image_paths = []
        for file_name in os.listdir(image_dir):
            if file_name.endswith(".jpeg"):
                self.image_paths.append(os.pardir.join(image_dir, file_name))


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


class text_net(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_size):
        super(text_net, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_size)

        def forward(self, x):
            x = self.embedding(x)
            _, (hidden, _) = self.lstm(x) 
            return self.fc(hidden[-1])
