from pyfirmata import Arduino , SERVO , util , o
import numpy as  np

import time

board = Arduino("/dev/cu.usbmodem14401")

iterator = util.Iterator(board)
iterator.start()




board.digital[9].mode = SERVO


def rotate(pin , angle) :
    board.digital[pin].write(angle)

result = [x for x in np.arange(10,180,2)]

for i in result :
    print(f"{round(i,1)} : degree")
    rotate(9,i)
    time.sleep(0.2)
