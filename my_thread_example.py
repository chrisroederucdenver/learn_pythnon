#!/usr/bin/env python3


import threading
import time 

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      print("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
#      time.sleep(delay)
      x = 0
      for i in range(1,100000000):
        x = x + i * 3.1415926
      print("%s: %s" % (threadName, time.ctime(time.time())) )
      counter -= 1



# Create new threads
thread1 = myThread(1, "Thread-1", 5)
thread2 = myThread(2, "Thread-2", 5)
thread3 = myThread(3, "Thread-3", 3)
thread4 = myThread(4, "Thread-4", 10)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

print("Exiting Main Thread")


