import pyfirmata
import time
import cv2
import serial


# Connect to Arduino
arduino = serial.Serial("COM3", 9600)


def process_frame(frame, results, x_mid, y_mid):

    detections = results.pandas().xyxy[0]  # Bounding box data

    if len(detections) > 0:
        frame_center_x = frame.shape[1] / 2
        frame_center_y = frame.shape[0] / 2
        # Determine direction based on object's position relative to frame center
        if x_mid < frame_center_x - 50:  # Object is left of center
            arduino.write(b"L")
        elif x_mid > frame_center_x + 50:  # Object is right of center
            arduino.write(b"R")
    
        if y_mid < 100:
            arduino.write(b"U")
        elif y_mid > 100:
            arduino.write(b"D")
