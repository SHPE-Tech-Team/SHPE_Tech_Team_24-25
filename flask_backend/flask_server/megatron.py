from ultralytics import YOLO
import cv2
import time
import os
import torch
import threading

# import aurdino


### for backedn
# def get_loteria():
#     model = YOLO("last.pt")
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Error With Camera")
#         return
#     try:
#         while True:
#             success, frame = cap.read()
#             if not success:
#                 print("Failed to grab frame")
#                 break
#             results = model(frame, conf=0.4)
#             annotated_frame = results[0].plot()
#             annotated_frame = coordinate_objects(results, annotated_frame)
#             ret, buffer = cv2.imencode(".jpg", annotated_frame)
#             frame_bytes = buffer.tobytes()
#             yield (
#                 b"--frame\r\n"
#                 b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
#             )
#             # delay for frame rate
#             time.sleep(0.03)
#     except Exception as e:
#         print(f"Error in video streaming: {e}")
#     finally:
#         cap.release()


##### new

class_color = {}
camera_class_ids = {}
tablas = [
    "tabla 1",
    "tabla 2",
    "tabla 3",
    "tabla 4",
    "tabla 5",
    "tabla 6",
    "tabla 7",
    "tabla 8",
    "tabla 9",
    "tabla 10",
]

green_cards = set()
def coordinate_objects(results, frame, shared_classes=None):
    detected_classes = set()
    
    total_cards = 16

    for result in results:
        boxes = result.boxes
        if boxes is not None:
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                x_mid = int((x1 + x2) / 2)
                y_mid = int((y1 + y2) / 2)
                conf = box.conf[0].item()
                cls = int(box.cls[0].item())

                detected_classes.add(cls)

                if cls not in tablas:
                    color = (0, 0, 255)  # Red
                    if class_color.get(cls) == True:
                        color = (0, 255, 0)  # Green
                    elif shared_classes and cls in shared_classes:
                        color = (0, 255, 0)  # Green
                        class_color[cls] = True  # Remember it was seen by both cameras
                        green_cards.add(cls)

                cv2.circle(frame, (x_mid, y_mid), 20, color, -1)
                cv2.putText(
                    frame,
                    f"({x_mid},{y_mid})",
                    (x_mid + 10, y_mid),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    color,
                    2,
                )

                print(
                    f"Camera sees class {cls}, confidence {conf:.2f}, midpoint ({x_mid},{y_mid})"
                )

    if green_cards == total_cards:
        cv2.putText(frame, "LOTERIA", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)
    # else:
    #     cv2.putText(frame, f"Cards: {len(green_cards)} /{total_cards}", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)

    return detected_classes


def testing_middle_dot():
    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "mps" if torch.backends.mps.is_available() else "cpu"
    )
    print(f"Using device: {device}")

    # model = YOLO("best.onnx", task="detect")

    model = YOLO("best.pt")  # for .pt
    model.to(device)  # for .pt

    cap0 = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(1)

    #  reduce resolution for better performance
    cap0.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap0.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # setting up lock
    frames = {}
    frames_lock = threading.Lock()
    running = True

    # skippinhg frames to reduce load
    skip_frames = 2

    def capture_process(cap, camera_id):
        nonlocal running
        frame_count = 0

        while running and cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print(f"Lost connection to Camera {camera_id}")
                break

            frame_count += 1
            if frame_count % skip_frames != 0:
                continue

            try:
                results = model(frame, conf=0.70)
                annotated_frame = results[0].plot()

                # Grab other camera's classes
                other_camera_id = 1 - camera_id
                with frames_lock:
                    shared_classes = camera_class_ids.get(other_camera_id, set())

                # Detect classes in this frame and draw
                detected_classes = coordinate_objects(
                    results, annotated_frame, shared_classes
                )

                # Save this frame and its detected classes
                with frames_lock:
                    frames[camera_id] = annotated_frame.copy()
                    camera_class_ids[camera_id] = detected_classes

            except Exception as e:
                print(f"Error processing frame from camera {camera_id}: {e}")

            time.sleep(0.001)

    threads = []
    if cap0.isOpened():
        threads.append(threading.Thread(target=capture_process, args=(cap0, 0)))
    if cap1.isOpened():
        threads.append(threading.Thread(target=capture_process, args=(cap1, 1)))

    for thread in threads:
        thread.daemon = True
        thread.start()

    try:
        last_frames = {}  # saving in case it is slow

        while running:
            frames_to_show = {}
            with frames_lock:
                frames_to_show = frames.copy()
                frames.clear()  # avoid memory build-up

            for camera_id, frame in frames_to_show.items():
                last_frames[camera_id] = frame

            # recent frames
            for camera_id, frame in last_frames.items():
                cv2.imshow(f"Camera {camera_id}", frame)

            # quit
            key = cv2.waitKey(10) & 0xFF
            if key == ord("q"):
                running = False
                break

            # releasing memory
            torch.cuda.empty_cache() if device.type == "cuda" else None
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        running = False
        print("Cleaning up resources...")

        # waiting for threads to finish
        for thread in threads:
            thread.join(timeout=1.0)

        cap0.release()
        cap1.release()
        cv2.destroyAllWindows()

        torch.cuda.empty_cache() if device.type == "cuda" else None
        print("Cleanup complete")


if __name__ == "__main__":
    testing_middle_dot()
