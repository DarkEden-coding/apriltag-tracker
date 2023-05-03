# move 2 stepper motors

import time
import RPi.GPIO as GPIO

# GPIO pins for the 2 motors
motor1_pins = (6, 13, 19, 26)
motor2_pins = (9, 11, 0, 5)

# GPIO setup
GPIO.setmode(GPIO.BOARD)
for pin in motor1_pins:
    print(pin)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

for pin in motor2_pins:
    print(pin)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


# motor1
def motor1(direction, steps):
    step = 0
    while step < steps:
        for pin in range(0, 4):
            GPIO.output(motor1_pins[pin], direction[step][pin])
        step += 1
        time.sleep(0.001)


# motor2
def motor2(direction, steps):
    step = 0
    while step < steps:
        for pin in range(0, 4):
            GPIO.output(motor2_pins[pin], direction[step][pin])
        step += 1
        time.sleep(0.001)


# clockwise
clockwise = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

# counterclockwise
counter_clockwise = [
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
]

# move motor1 clockwise 2048 steps
motor1(clockwise, 2048)

# move motor2 counterclockwise 2048 steps
motor2(counter_clockwise, 2048)
