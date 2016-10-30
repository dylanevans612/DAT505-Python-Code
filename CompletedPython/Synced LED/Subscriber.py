from mosquitto import *
from serial import *
from random import *

def dataReceived(broker, obj, msg):
    global client
    receive_data = msg.payload.decode()
    if(receive_data == "OFF"):
        data = "0"
        
    else:
        data = "1"

        board.write(data.encode())
        
# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino
board = Serial("COM5",115200,timeout=2)

randomID = random()
client = Mosquitto("LightSubscriber" + str(randomID))
client.connect("10.212.61.136")
client.on_data = dataReceived


while(True): client.loop()