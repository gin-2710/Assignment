# Question 2: Do django signals run in the same thread as the caller?

# Answer:
# Django signals run in the same thread as the caller. 
# Due to this, the signal receiver functions execute within the same thread as the code that triggered the signal

#Example is provided below

from django.dispatch import Signal
import threading
import time

signal = Signal()

def receiver1(sender, **kwargs):
    print("Receiver 1 started", threading.get_ident())
    time.sleep(2)
    print("Receiver 1 finished", threading.get_ident())

def receiver2(sender, **kwargs):
    print("Receiver 2 started", threading.get_ident())
    print("Receiver 2 finished", threading.get_ident())

def trigger_signal():
    print("Triggering signal in thread:", threading.get_ident())
    signal.send(None)
    print("Signal sent in thread:", threading.get_ident())

thread = threading.Thread(target=trigger_signal)

signal.connect(receiver1)
signal.connect(receiver2)

thread.start()

thread.join()