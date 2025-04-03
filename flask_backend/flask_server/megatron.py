from ultralytics import YOLO
import cv2
import time
import os
import torch
import threading

# import aurdino


### for backedn
def get_loteria():
    model = YOLO("last.pt")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error With Camera")
        return
    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("Failed to grab frame")
                break
            results = model(frame, conf=0.4)
            annotated_frame = results[0].plot()
            annotated_frame = coordinate_objects(results, annotated_frame)
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


def coordinate_objects(results, frame):

    for result in results:
        boxes = result.boxes
        if boxes is not None:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                x_mid = int((x1 + x2) / 2)
                y_mid = int((y1 + y2) / 2)
                conf = box.conf[0].item()
                cls = int(box.cls[0].item())

                # Draw a circle at the middle point (red color, 5px radius, filled)
                cv2.circle(frame, (x_mid, y_mid), 20, (0, 0, 255), -1)

                # aurdino.process_frame(frame, results, x_mid, y_mid)

                # Optional: Add text label showing coordinates
                cv2.putText(
                    frame,
                    f"({x_mid},{y_mid})",
                    (x_mid + 10, y_mid),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2,
                )

                print(f"Coordinates: ({x1}, {y1}), ({x2}, {y2})")
                print(f"middle: ({x_mid}, {y_mid})")
                print(f"Confidence: {conf}")
                print(f"Class: {cls}")

### works finneeee
# def camera_condition(model, has_cam, cap):
#     if has_cam:
#         ret, frame = cap.read()
#     if ret:
#         results = model(frame, conf=0.4)
#         annotated_frame = results[0].plot()
#         coordinate_objects(results, annotated_frame)
#         cv2.imshow("Webcam", annotated_frame)
#     else:
#         print("Lost connection")
#         cap.release()
#         has_cam = False
#     return has_cam


# ### works fine
# def testing_middle_dot():
#     # load model
#     model = YOLO("best.pt")

#     # Try to open both cameras
#     cap0 = cv2.VideoCapture(0)
#     cap1 = cv2.VideoCapture(0)

#     has_cam0 = cap0.isOpened()
#     has_cam1 = cap1.isOpened()

#     if not has_cam0 and not has_cam1:
#         print("No cameras detected. Exiting...")
#         exit()

#     while has_cam0 or has_cam1:
#         if has_cam0:
#             has_cam0 = camera_condition(model, has_cam0, cap0)
#         if has_cam1:
#             has_cam1 = camera_condition(model, has_cam1, cap1)

#         # Exit loop on 'q' press
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break

#     # Release resources
#     if has_cam0:
#         cap0.release()
#     if has_cam1:
#         cap1.release()
#     cv2.destroyAllWindows()


# def process_camera(model, cap, camera_id):
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if ret:

#             results = model(frame, conf=0.4)
#             annotated_frame = results[0].plot()
#             coordinate_objects(results, annotated_frame)
#             cv2.imshow(f"Camera {camera_id}", annotated_frame)
#         else:
#             print(f"Lost connection to Camera {camera_id}")
#             break

#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break

#     cap.release()


# def testing_middle_dot():
#     model = YOLO("last.pt")

#     cap0 = cv2.VideoCapture(0)
#     cap1 = cv2.VideoCapture(1)

#     threads = []
#     if cap0.isOpened():
#         threads.append(threading.Thread(target=process_camera, args=(model, cap0, 0)))
#     if cap1.isOpened():
#         threads.append(threading.Thread(target=process_camera, args=(model, cap1, 1)))

#     for thread in threads:
#         thread.start()

#     for thread in threads:
#         thread.join()

#     cv2.destroyAllWindows()


def testing_middle_dot():
    model = YOLO("best.pt")
    cap0 = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(1)

    # Shared data between threads
    frames = {}
    running = True

    def capture_process(cap, camera_id):
        nonlocal running
        while running and cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print(f"Lost connection to Camera {camera_id}")
                break

            results = model(frame, conf=0.4)
            annotated_frame = results[0].plot()
            coordinate_objects(results, annotated_frame)

            # Store frame for display in main thread
            frames[camera_id] = annotated_frame

    threads = []
    if cap0.isOpened():
        threads.append(threading.Thread(target=capture_process, args=(cap0, 0)))
    if cap1.isOpened():
        threads.append(threading.Thread(target=capture_process, args=(cap1, 1)))

    for thread in threads:
        thread.start()

    # Main thread handles the display
    try:
        while running:
            # Display any available frames
            for camera_id, frame in list(frames.items()):
                cv2.imshow(f"Camera {camera_id}", frame)

            # q to quit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                running = False
                break

            time.sleep(0.01)  # Small delay to prevent CPU hogging
    finally:
        running = False
        for thread in threads:
            thread.join()

        cap0.release()
        cap1.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "mps" if torch.backends.mps.is_available() else "cpu"
    )
    print(f"Using device: {device}")

    testing_middle_dot()
