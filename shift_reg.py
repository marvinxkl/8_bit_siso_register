import RPi.GPIO as IO   
import time             
IO.setwarnings(False)  

ser = 4
sck = 5
rck = 6

IO.setmode(IO.BCM)      
IO.setup(ser,IO.OUT)      # pin 4 as output (SER)
IO.setup(sck,IO.OUT)      # pin 4 as output (SCK)
IO.setup(rck,IO.OUT)      # pin 4 as output (RCK)

pins = [0,0,0,0,0,0,0,0]


def pinOnInRow(i, t=0.1):
    pinsAllOff()
    global ser, sck, rck
    for y in range(i):    
        shiftRegistry(1,0)
        IO.output(ser,1)  # send a 1 to seriell input 
        time.sleep(t)     
        IO.output(sck,1)  # sck high to shift the bits
        time.sleep(t)     
        IO.output(sck,0)  
        IO.output(ser,0)  
        IO.output(rck,1)  # rck high to send the output
        time.sleep(t)     
        IO.output(rck,0)  # rck low to stop the output
        

def pinOffInRow(i, t=0.1):
    global ser, sck, rck
    for y in range(i):    
        shiftRegistry(0,0)
        IO.output(ser,0)    # send a 0 to seriell input
        time.sleep(t)     
        IO.output(sck,1)    # sck high to shift the bits
        time.sleep(t)     
        IO.output(sck,0)    
        IO.output(ser,0)    
        IO.output(rck,1)    # rck high to send the output
        time.sleep(t)     
        IO.output(rck,0)    # rck low to stop the output

     
def pinsOnBin(i):
    global pins
    for y in reversed(range(8)):
        pins [y] = i%2
        i = i//2
    sendRegistry()
        
# Turn required pin on
def pinOnAt(i):
    global pins
    if pins[i-1] == 1:
        print("pin already high")
    else:
        pins[i-1] = 1;
        sendRegistry()
        
def pinsAllOff():
    global pins
    pins = [0,0,0,0,0,0,0,0]
    sendRegistry()
        
def shift(i):
    global sck
    for y in range(i):
        IO.output(sck,1)  # sck high to shift the bits
        IO.output(sck,0)
        
def send():
    global rck
    IO.output(rck,1)  # rck high to send the output
    IO.output(rck,0)  # rck low to stop the output
    
    
def shiftRegistry(condition, pin):
    global pins
    tempPins = pins [:]
    for i in range(7):
        pins [i+1] = tempPins[i]
    pins[pin] = condition
    
def sendRegistry():
    global pins, ser
    for y in reversed(range(8)):
        if pins[y] == 1:
            IO.output(ser,1)
        else:
            IO.output(ser,0)
        shift(1)
    send()
            
    
