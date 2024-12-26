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
from tokenizers import Tokenizer
from tqdm.auto import tqdm
import torch.optim as optim
from torch.nn.utils.rnn import pad_sequence
from torch.nn import functional as F


class Dataset_Setup:
    def __init__(self, image_dir, image_transform=None, text_tokenizer=None):
        self.image_dir = image_dir
        self.image_transform = image_transform
        self.text_tokenizer = text_tokenizer
        self.image_paths = []
        for file_name in os.listdir(image_dir):
            if file_name.endswith(".jpeg"):
                self.image_paths.append(os.path.join(image_dir, file_name))

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        image = Image.open(image_path).convert("RGB")
        text = pytesseract.image_to_string(image)

        if self.image_transform:
            image = self.image_transform(image)

        if self.text_tokenizer:
            text = self.text_tokenizer(text)

        return image, text


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
    def __init__(
        self, vocab_size, embedding_dim, hidden_dim, output_size, max_text_length
    ):
        super(text_net, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_size)
        self.max_text_length = max_text_length

    def forward(self, x):
        x = self.embedding(x)
        x = F.pad(
            x, (0, self.max_text_length - x.size(1))
        )  # Pad sequence to max length
        _, (hidden, _) = self.lstm(x)
        return self.fc(hidden[-1])


class HybridNetwork(nn.Module):
    def __init__(self, image_model, text_model, combined_output_size, num_classes):
        super(HybridNetwork, self).__init__()
        self.image_model = image_model
        self.text_model = text_model
        self.fc = nn.Sequential(
            nn.Linear(combined_output_size, 512), nn.ReLU(), nn.Linear(512, num_classes)
        )

    def forward(self, image, text):
        image_features = self.image_model(image)
        text_features = self.text_model(text)
        combined_features = torch.cat((image_features, text_features), dim=-1)
        return self.fc(combined_features)


if __name__ == "__main__":

    def simple_tokenizer(text):
        return text.split()

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

    train_set = Dataset_Setup(
        image_dir="/Users/laflame/SHPE TECH TEAM AI/AI_Loteria_24-25/loteria_dataset",
        image_transform=train_transform,
        text_tokenizer=simple_tokenizer,
    )

    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

    vocab_size = 5000  # Example size, adjust according to your tokenizer
    embedding_dim = 128
    hidden_dim = 256
    num_classes = 100
    combined_output_size = num_classes + hidden_dim

    image_model = Network(num_classes=num_classes)
    text_model = text_net(
        vocab_size=vocab_size,
        embedding_dim=embedding_dim,
        hidden_dim=hidden_dim,
        output_size=num_classes,
        max_text_length=50,
    )

    model = HybridNetwork(
        image_model=image_model,
        text_model=text_model,
        combined_output_size=combined_output_size,
        num_classes=num_classes,
    )
    batch_size = 32
    train_loader = DataLoader(
        train_set, batch_size=batch_size, shuffle=True, num_workers=0
    )
    num_epochs = 10
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    lr_scheduler = lrs.StepLR(optimizer, step_size=5, gamma=0.1)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(num_epochs):  # Make sure `num_epochs` is defined
        model.train()

        it_train = tqdm(
            enumerate(train_loader),
            total=len(train_loader),
            desc="Training ...",
            position=0,
        )

        for batch_idx, (images, texts) in it_train:
            # Preprocess text (tokenize it)
            # Ensure tokenization function is appropriate
            tokenized_texts = [simple_tokenizer(text) for text in texts]

            # Convert tokenized texts to tensor format if necessary
            # For example, you could use padding or embeddings for your text
            tokenized_texts = [
                torch.tensor(text) for text in tokenized_texts
            ]  # Example, adjust as needed

            # Move data to device (GPU/CPU)
            images = images.to(device)  # Make sure `device` is defined
            tokenized_texts = [text.to(device) for text in tokenized_texts]

            # Forward pass through the hybrid model
            outputs = model(images, tokenized_texts)

            # Assuming labels are provided in the dataset
            labels = texts  # Example, change as per your actual dataset structure

            # Compute the loss
            loss = criterion(outputs, labels)

            # Backpropagation and optimization
            optimizer.zero_grad()  # Zero gradients from the previous step
            loss.backward()  # Backpropagate the loss
            optimizer.step()  # Update model weights

            # Update learning rate
            lr_scheduler.step()  # Step the learning rate scheduler

            # Print loss for tracking progress
            it_train.set_description(f"Epoch {epoch + 1}, Loss: {loss.item():.4f}")
