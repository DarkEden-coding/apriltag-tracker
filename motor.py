import RPi.GPIO as GPIO
import time


class Motor:
    """
    A class to represent a stepper motor that tracks motor position.
    """

    def __init__(self, pin1, pin2, pin3, pin4):
        """
        Constructs all the necessary attributes for the stepper motor object.
        :param pin1: gpio pin number for IN1
        :param pin2: gpio pin number for IN2
        :param pin3: gpio pin number for IN3
        :param pin4: gpio pin number for IN4
        """
        self.IN1 = pin1
        self.IN2 = pin2
        self.IN3 = pin3
        self.IN4 = pin4
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        self.sequence = [
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
        ]
        self.position = 0

    def move(self, steps, direction):
        for i in range(steps):
            for step in range(8):
                # Set the motor pins according to the current step in the sequence
                GPIO.output(self.IN1, self.sequence[step][0])
                GPIO.output(self.IN2, self.sequence[step][1])
                GPIO.output(self.IN3, self.sequence[step][2])
                GPIO.output(self.IN4, self.sequence[step][3])
                # Wait a short amount of time between each step
                time.sleep(0.001)
            # Reverse the sequence if moving backwards
            # Reverse the sequence if moving backwards
            if direction == "backward":
                self.sequence.reverse()
                self.position -= 1
            else:
                self.position += 1

    def get_position(self):
        return self.position

    def disable(self):
        GPIO.cleanup((self.IN1, self.IN2, self.IN3, self.IN4))
