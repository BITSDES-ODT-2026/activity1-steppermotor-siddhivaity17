from machine import Pin
import time

A = Pin(32, Pin.OUT)
B = Pin(25, Pin.OUT)
C = Pin(5, Pin.OUT)
D = Pin(19, Pin.OUT)
pos= [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    for i in pos:
        A.value(i[0])
        B.value(i[1])
        C.value(i[2])
        D.value(i[3])
        time.sleep(0.005)
        print("kuchbhi")
        
