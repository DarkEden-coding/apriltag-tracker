import RPi.GPIO as GPIO
import time

# Define the motor pin numbers
IN1 = 26
IN2 = 19
IN3 = 13
IN4 = 6

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Define the sequence of steps
# Each row represents a step, and the columns are the IN1-IN4 pin states
# This sequence will rotate the motor clockwise
sequence = [[1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]]


# Define a function to move the motor a specified number of steps in a given direction
def move_motor(steps, direction):
    for i in range(steps):
        for step in range(8):
            # Set the motor pins according to the current step in the sequence
            GPIO.output(IN1, sequence[step][0])
            GPIO.output(IN2, sequence[step][1])
            GPIO.output(IN3, sequence[step][2])
            GPIO.output(IN4, sequence[step][3])
            # Wait a short amount of time between each step
            time.sleep(0.001)
        # Reverse the sequence if moving backwards
        if direction == 'backward':
            sequence.reverse()


# Move the motor forward 100 steps
move_motor(2000, 'forward')
time.sleep(1)

# Move the motor backward 100 steps
move_motor(2000, 'backward')
time.sleep(1)

# Clean up the GPIO pins
GPIO.cleanup()
