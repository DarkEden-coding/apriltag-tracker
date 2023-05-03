from RpiMotorLib import RpiMotorLib
import time
import RPi.GPIO as GPIO

# Declare an named instance of class pass your custom name and type of motor
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
motor2_pins = (9, 11, 0, 5)


def main():
    GpioPins = [26, 19, 13, 6]

    # Arguments  for motor run function
    # (GPIOPins, stepdelay, steps, counterclockwise, verbose, steptype, initdelay)

    for i in range(10):
        if i % 2 == 0:
            time.sleep(0.1)
            mymotortest.motor_run(GpioPins, 0.05, 128, True, False, "full", 0.05)
        else:
            time.sleep(0.1)
            mymotortest.motor_run(GpioPins, 0.05, 128, False, False, "full", 0.05)


# ===================MAIN===============================

if __name__ == "__main__":
    print("START")
    GPIO.setmode(GPIO.BCM)
    main()
    GPIO.cleanup()  # Optional
    exit()

# =====================END===============================
