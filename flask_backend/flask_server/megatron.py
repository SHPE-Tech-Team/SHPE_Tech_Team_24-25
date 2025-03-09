from ultralytics import YOLO
import cv2
import time


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
