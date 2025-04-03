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


def testing_middle_dot(device=None):
    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "mps" if torch.backends.mps.is_available() else "cpu"
    )
    print(f"Using device: {device}")

    model = YOLO("best.pt")
    model.to(device)

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
            if frame_count % skip_frames != 0:  # skipping frames
                continue

            try:
                
                results = model(frame, conf=0.9)
                annotated_frame = results[0].plot()
                coordinate_objects(results, annotated_frame)

                # store frame for display in main thread
                with frames_lock:
                    frames[camera_id] = (
                        annotated_frame.copy()
                    ) 

            except Exception as e:
                print(f"Error processing frame from camera {camera_id}: {e}")

            # small delay to prevent hogging
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
        last_frames = {}  #saving in case it is slow

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

            #releasing memory
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
