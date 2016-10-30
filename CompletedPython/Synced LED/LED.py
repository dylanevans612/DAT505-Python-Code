from microbit import *

while(True):
    if(uart.any()):
        input = uart.readline()
        uart.write(" Good day to you sir !\n")