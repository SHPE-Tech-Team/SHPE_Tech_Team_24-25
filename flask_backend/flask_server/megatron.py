from ultralytics import YOLO
import cv2
import time
import os


def train_model(
    data_path="data.yaml", epochs=100, imgsz=640, batch=16, model_name="yolov8_custom"
):
    """
    Train a YOLO model and save it for later use.

    Args:
        data_path: Path to data.yaml config file
        epochs: Number of training epochs
        imgsz: Image size for training
        batch: Batch size
        model_name: Name for the training run

    Returns:
        Path to the best weights file
    """
    # Initialize with pre-trained weights
    model = YOLO("yolov8n.pt")

    if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data file not found: {os.path.abspath(data_path)}")

    # Train the model
    results = model.train(
        data=data_path, epochs=epochs, imgsz=imgsz, batch=batch, name=model_name
    )

    # Get path to best weights
    best_weights_path = os.path.join("runs/detect", model_name, "weights", "best.pt")
    print(f"Training complete. Best model saved at: {best_weights_path}")

    return best_weights_path


def get_loteria():
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(0) 
    if not cap.isOpened():
        print("Error: Camera not accessible")
        return
    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("Failed to grab frame")
                break
            results = model(frame, conf=0.4)
            annotated_frame = results[0].plot()
            ret, buffer = cv2.imencode(".jpg", annotated_frame)
            frame_bytes = buffer.tobytes()
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
            )
            # delay for frame rate
            time.sleep(0.03)
    except Exception as e:
        print(f"Error in video streaming: {e}")
    finally:
        cap.release()


if __name__ == "__main__":
    # To train the model:
    print(f"Current working directory: {os.getcwd()}")

    # Find the correct path to your data.yaml file
    # possible_paths = [
    #     "My-First-Project-2/data.yaml",  # If in same directory as script
    #     "flask_server/My-First-Project-2/data.yaml",  # If relative to flask_backend
    #     "../My-First-Project-2/data.yaml",  # If one level up
    #     "./My-First-Project-2/data.yaml",  # Explicit current directory
    # ]

    # data_path = None
    # for path in possible_paths:
    #     if os.path.exists(path):
    #         data_path = path
    #         break

    # if not data_path:
    #     print("Could not find data.yaml file. Please provide the correct path.")
    # else:
    # print(f"Found data.yaml at: {"flask_backend/flask_server/data.yaml"}")
    saved_model_path = train_model(data_path="flask_backend/flask_server/data.yaml")
    print(f"Model saved at: {saved_model_path}")
