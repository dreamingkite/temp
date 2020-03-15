import threading
import logging
import time
logging.basicConfig(level=logging.INFO)


class A:
    def __init__(self,x):
        self.x = x

a = A(10)

x = 10

def change():
    x = x + 1
    print(x)

change()