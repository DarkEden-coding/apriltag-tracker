import cv2
from apriltag import get_tag
from motor import Motor

motor_yaw = Motor(6, 13, 19, 26)
motor_pitch = Motor(9, 11, 0, 5)

# capture camera frames
cap = cv2.VideoCapture(0)

# loop through frames
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cx, cy = get_tag(frame)

        if cx is not None and cy is not None:
            print(cx, cy)
            yaw_direction = "foward" if cx > 0 else "backward"
            pitch_direction = "foward" if cy > 0 else "backward"
            # motor_yaw.move(cx, yaw_direction)
            # motor_pitch.move(cy, pitch_direction)
