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
import cv2
from CNN_SHPE import Network


classes = [
    "LA BOTELLA",
    "LA RANA",
    "EL ARPA",
    "LA GARZA",
    "EL MELON",
    "LA DAMA",
    "LA MANO",
    "EL PAJARO",
    "LA CORONA",
    "LA SANDIA",
    "LA LUNA",
    "EL COTORRO",
    "LA BOTA",
    "EL ARBOL",
    "EL VIOLONCELLO",
    "EL NEGRITO",
    "EL SOLDADO",
    "EL VALIENTE",
    "EL GORRITO",
    "LA MUERTE",
    "LA PERA",
    "EL MUSICO",
    "EL CAMARON",
    "EL TAMBOR",
    "EL CANTARITO",
    "EL DIABLITO",
    "LA CHALUPA",
    "EL SOL",
    "EL VENADO",
    "LA ROSA",
    "EL PINO",
    "EL BARRIL",
    "EL BANDOLON",
    "EL GALLO",
    "EL BORRACHO",
    "LA ARAÑA",
    "LA MACETA",
    "LA PALMA",
    "EL PESCADO",
    "LA BANDERA",
    "LA CAMPANA",
    "LA ESTRELLA",
    "EL CORAZON",
    "EL APACHE",
    "EL MUNDO",
    "EL CAZO",
    "LAS JARAS",
    "EL NOPAL",
    "EL ALACRAN",
    "EL CALAVERA",
    "EL PARAGUAS",
    "EL CATRIN",
    "LA ESCALERA",
    "LA SIRENA",
]

# checking device
device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "mps" if torch.backends.mps.is_available() else "cpu"
)
print(f"Using device: {device}")
model = Network(num_classes=54)
checkpoint = torch.load("final_model.pth", weights_only=True)
model_state_dict = checkpoint["model_state_dict"]
model.load_state_dict(model_state_dict)
model.to(device)
model.eval()
cam = cv2.VideoCapture(0)


transform = transforms.Compose(
    [
        transforms.ToPILImage(),
        transforms.Resize((256, 256)),
        transforms.CenterCrop((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)



def __draw_label(img, text, pos, bg_color):
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    color = (0, 0, 0)
    thickness = 2
    margin = 5
    txt_size = cv2.getTextSize(text, font_face, scale, thickness)

    end_x = pos[0] + txt_size[0][0] + margin * 2
    end_y = pos[1] - txt_size[0][1] - margin * 2

    cv2.rectangle(img, (pos[0], end_y), (end_x, pos[1]), bg_color, -1)
    text_pos = (pos[0] + margin, pos[1] - margin)

    cv2.putText(img, text, text_pos, font_face, scale, color, thickness, cv2.LINE_AA)


def frame_proccessing(frame, model, transform, device, min_confidence=0.2):
    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # apply adaptive thresholding
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )

    # find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # sort contours by area (largest first)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # only process the largest contour that meets minimum size requirements
    for contour in contours[:1]:  # only look at the largest contour
        area = cv2.contourArea(contour)
        if area < 1000:  # minimum area threshold
            continue

        # bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)

        # checking aspect ratio
        aspect_ratio = w / h
        if not (0.5 <= aspect_ratio <= 2.0):  # Skip if aspect ratio is too extreme
            continue

        # expanding the box
        padding = 20
        x1 = max(0, x - padding)
        y1 = max(0, y - padding)
        x2 = min(frame.shape[1], x + w + padding)
        y2 = min(frame.shape[0], y + h + padding)

        # cropping image
        cropped = frame[y1:y2, x1:x2]
        if cropped.size == 0:
            continue

        # preparing input tensor for model
        input_tensor = transform(cropped).unsqueeze(0).to(device)

        # model predicts
        with torch.no_grad():
            outputs = model(input_tensor)
            probabilities = F.softmax(outputs, dim=1)
            confidence, predicted_idx = torch.max(probabilities, 1)

            # only display prediction if confidence is high enough
            if confidence.item() > min_confidence:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{classes[predicted_idx.item()]} ({confidence.item():.2f})"
                __draw_label(frame, label, (x1, y1 - 10), (255, 255, 255))
    return frame


while True:
    ret, frame = cam.read()
    if not ret:
        break

    processed_frame = frame_proccessing(frame, model, transform, device)
    cv2.imshow("preview", processed_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
