from microbit import *

uart.write("Ready\n")
while(True):
    if(uart.any()):
        input = uart.read(1)
        next_character = chr(input[0])
        print("You just sent: " + next_character)

        microbit.display.get_pixel(x,y)
        microbit.display.set_pixel(x, y, value)
        microbit.display.clear()
        microbit.display.show(image)
        microbit.display.show