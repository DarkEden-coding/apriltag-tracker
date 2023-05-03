from rpimotorlib import Motor
import time

# Define motor pins
motor1_pins = (6, 13, 19, 26)
motor2_pins = (9, 11, 0, 5)

# Create Motor objects
motor1 = Motor(motor1_pins)
motor2 = Motor(motor2_pins)

# Move both motors 90 degrees back and forth
for i in range(2):
    motor1.move_steps(2000, direction='backward')
    motor2.move_steps(2000, direction='backward')
    time.sleep(1)
    motor1.move_steps(2000, direction='forward')
    motor2.move_steps(2000, direction='forward')
    time.sleep(1)

# Cleanup motors
motor1.cleanup()
motor2.cleanup()
