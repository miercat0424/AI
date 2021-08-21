
from pyfirmata import Arduino
from time import sleep
import os

def dcMotorControl(r, deltaT,dir=1):

    if dir == -1 :
        print("CW")
        for ii in range(r+1) :
            pwmPin3.write(ii/100.00)
            print(f"{ii} : Power")
            sleep(0.02)
        print(f"Max Power : {ii}")

        for times in range(deltaT) :
            print(f"{deltaT - times} seconds left")
            sleep(1)
        pwmPin3.write(0)
        sleep(1)

    else : 
        print("CCW")
        for ii in range(r+1) :
            pwmPin5.write(ii/100.00)
            print(f"{ii} : Power")
            sleep(0.02)
        print(f"Max Power : {ii}")

        for times in range(deltaT) :
            print(f"{deltaT - times} seconds left")
            sleep(1)
        pwmPin5.write(0)
        sleep(1)
        




board = Arduino("/dev/cu.usbmodem14401")


# set mode of pin 3 as PWM
pwmPin3 = board.get_pin('d:3:p')
pwmPin5 = board.get_pin('d:5:p')

try:
    while True:
        r = int(input("Enter value to set motor speed : "))
        if r > 100 or r <= 0  :
            print("betwee 0 to 100 only")
            board.exit()
            break
        t = int(input("How long? in seconds : "))
        dcMotorControl(r, t)

except KeyboardInterrupt:
    board.exit()
    os._exit


