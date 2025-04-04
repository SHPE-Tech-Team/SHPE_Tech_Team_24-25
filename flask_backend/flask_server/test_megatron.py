from roboflow import Roboflow
from ultralytics import YOLO
import os
import sys
import torch
from dotenv import load_dotenv
import os


def download_dataset():
    version = 8
    load_dotenv()
    api_key = os.getenv("API_KEY")
    try:
        rf = Roboflow(api_key=api_key)
        project = rf.workspace("loteria").project("loteria-dataset")
        version = project.version(version)
        dataset = version.download("yolov8")

        # Extract the actual path from the dataset object
        dataset_dir = str(dataset.location)
        print(f"Dataset downloaded to {dataset_dir}")

        # Verify the directory exists
        if not os.path.exists(dataset_dir):
            raise FileNotFoundError(f"Dataset directory not found: {dataset_dir}")

        return dataset_dir
    except Exception as e:
        print(f"Error downloading dataset: {str(e)}")
        sys.exit(1)


def train_model():
    try:
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        print(f"Using device: {device}")

        dataset_dir = download_dataset()
        yaml_path = os.path.join(dataset_dir, "data.yaml")

        if not os.path.exists(yaml_path):
            print(f"YAML file not found at {yaml_path}")
            print(f"Contents of {dataset_dir}:")
            for item in os.listdir(dataset_dir):
                print(f"  - {item}")
            raise FileNotFoundError(f"YAML file not found: {yaml_path}")

        print(f"YAML path confirmed: {yaml_path}")

        model = YOLO("yolov8n.pt")  

        results = model.train(
            data=yaml_path,
            epochs=25,
            imgsz=640,
            batch=-1,
            device=device,
            lr0=0.001,
            optimizer="AdamW",
            weight_decay=0.05,
            name="loteria_model",
            save_period=5,
        )

        model_path = os.path.join(
            "runs", "detect", "loteria_model", "weights", "best.pt"
        )
        print(f"Model saved at: {model_path}")

        print("Training completed successfully!")
        return model
    except Exception as e:
        print(f"Error during model training: {str(e)}")
        sys.exit(1)


def test_inference(model_path="runs/detect/loteria_model/weights/best.pt"):
    """Test the trained model with a simple inference"""
    try:
        if not os.path.exists(model_path):
            print(f"Model file not found at {model_path}")
            return

        # Load the trained model
        model = YOLO(model_path)
        print(f"Model loaded successfully from {model_path}")

        # You can add test inference code here
        print("Model ready for inference")
        return model
    except Exception as e:
        print(f"Error loading model: {str(e)}")


if __name__ == "__main__":
    # Train the model
    trained_model = train_model()
    trained_model.export(format="onnx")
    # Test loading the saved model
    test_inference()
