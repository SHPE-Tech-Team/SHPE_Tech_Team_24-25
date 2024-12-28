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


device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "mps" if torch.backends.mps.is_available() else "cpu"
)
print(f"Using device: {device}")
model = Network(num_classes=54)
checkpoint = torch.load("final_model.pth", weights_only=True)
# Extract the model state dict
model_state_dict = checkpoint["model_state_dict"]

# Load the state dict into your model
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
    thickness = 10
    margin = 2
    txt_size = cv2.getTextSize(text, font_face, scale, thickness)

    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] - margin

    cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
    cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)
while True:
    ret, frame = cam.read()

    if not ret:
        break

    # covert it to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # contours in the frame
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # looping through contours and drawing bounding boxes
    for contour in contours:
        # Filter by contour size (optional)
        if cv2.contourArea(contour) > 500:  # Adjust the area threshold as needed
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Crop the detected region and preprocess it for the model
            cropped = frame[y : y + h, x : x + w]
            input_tensor = transform(cropped).unsqueeze(0).to(device)

            # Make prediction
            with torch.no_grad():
                prediction = model(input_tensor)

            _, predicted_idx = torch.max(prediction, 1)
            predicted_label = f"Class {classes[predicted_idx.item()]}"

            # drawing label on the box
            __draw_label(frame, predicted_label, (x, y - 10), (255, 255, 255))

    # update framw
    cv2.imshow("preview", frame)

    # breaking loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
