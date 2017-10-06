#Author: OMKAR PATHAK
#This script helps to build a simple stopwatch application using Python's time module.

from time import time

print('Press ENTER to begin, Press Ctrl + C to stop')
while True:
    try:
        input() # For ENTER. Use raw_input() if you are running python 2.x instead of input()
        starttime = time()
        print('Started')
    except KeyboardInterrupt:
        print('Stopped')
        endtime = time()
        print('Total Time:', round(endtime - starttime, 2),'secs')
        break
