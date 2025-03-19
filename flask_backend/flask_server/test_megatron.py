from roboflow import Roboflow
from ultralytics import YOLO
import os
import sys





                
def download_dataset():
    try:
        rf = Roboflow(api_key="xIGN2O5hVPAzGUvmfhC7")
        project = rf.workspace("loteria").project("my-first-project-a9nmn")
        version = project.version(2)
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
        dataset_dir = download_dataset()
        # Define path to the YAML file which is typically in the downloaded directory
        yaml_path = os.path.join(dataset_dir, "data.yaml")

        if not os.path.exists(yaml_path):
            print(f"YAML file not found at {yaml_path}")
            print(f"Contents of {dataset_dir}:")
            for item in os.listdir(dataset_dir):
                print(f"  - {item}")
            raise FileNotFoundError(f"YAML file not found: {yaml_path}")

        print(f"YAML path confirmed: {yaml_path}")

        # Initialize the YOLO model
        # Using a pretrained model for better results
        model = YOLO("yolov8n.pt")  # start from pretrained model

        # Train the model
        results = model.train(
            data=yaml_path, epochs=100, imgsz=640, batch=8, name="loteria_model"
        )

        # Get path to the saved model (best weights)
        model_path = os.path.join(
            "runs", "detect", "loteria_model", "weights", "best.pt"
        )
        print(f"Model saved at: {model_path}")

        # Explicitly save the model if needed
        # model.save('loteria_model_final.pt')

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

    # Test loading the saved model
    test_inference()
