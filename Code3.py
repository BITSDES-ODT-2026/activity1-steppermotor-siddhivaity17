from machine import Pin
import time

IN1 = Pin(32,Pin.OUT)
IN2 = Pin(25, Pin.OUT)
IN3 = Pin(5,Pin.OUT)
IN4 = Pin(19,Pin.OUT)
my_t = 2


pos = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    
    for i in range(500):
        for i in pos:
            IN1.value(i[0])
            
            IN2.value(i[1])
            
            IN3.value(i[2])
            
            IN4.value(i[3])
            
            time.sleep_ms(my_t)
            
    for i in range(500):
        for i in reversed(pos):
        
            IN1.value(i[0])
            
            IN2.value(i[1])
            
            IN3.value(i[2])
            
            IN4.value(i[3])
            
            time.sleep_ms(my_t)

