# Question 1: By default are django signals executed synchronously or asynchronously?

# Answer:
# Django signals are executed synchronously by default. 

#Example is provided below

from django.dispatch import Signal
import time

signal = Signal()

def receiver1(sender, **kwargs):
    print("Receiver 1 started")
    time.sleep(3)
    print("Receiver 1 finished")

def receiver2(sender, **kwargs):
    print("Receiver 2 started")
    print("Receiver 2 finished")

signal.connect(receiver1)
signal.connect(receiver2)

print("Sending signal...")
signal.send(None)
print("Signal sent")