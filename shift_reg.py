import RPi.GPIO as __IO   
import time as __time            
__IO.setwarnings(False)  


__ser = 4
__sck = 5
__rck = 6

__IO.setmode(IO.BCM)      
__IO.setup(__ser,IO.OUT)      # pin 4 as output (SER)
__IO.setup(__sck,IO.OUT)      # pin 5 as output (SCK)
__IO.setup(__rck,IO.OUT)      # pin 6 as output (RCK)

__pins = [0,0,0,0,0,0,0,0]


def pins_on_in_a_row(i, t=0.1):
    pinsAllOff()
    global __ser, __sck, __rck
    for y in range(i):    
        __shiftRegistry(1,0)
        __IO.output(__ser,1)  # send a 1 to seriell input 
        __time.sleep(t)     
        __IO.output(__sck,1)  # sck high to shift the bits
        __time.sleep(t)     
        __IO.output(__sck,0)  
        __IO.output(__ser,0)  
        __IO.output(__rck,1)  # rck high to send the output
        __time.sleep(t)     
        __IO.output(__rck,0)  # rck low to stop the output
        

def pin_off_in_a_rowi, t=0.1):
    global __ser, __sck, __rck
    for y in range(i):    
        __shiftRegistry(0,0)
        __IO.output(__ser,0)    # send a 0 to seriell input
        __time.sleep(t)     
        __IO.output(__sck,1)    # sck high to shift the bits
        __time.sleep(t)     
        __IO.output(__sck,0)    
        __IO.output(__ser,0)    
        __IO.output(__rck,1)    # rck high to send the output
        __time.sleep(t)     
        __IO.output(__rck,0)    # rck low to stop the output

        
def pins_on_binary(i):
    global __pins
    for y in reversed(range(8)):
        __pins [y] = i%2
        i = i//2
    __sendRegistry()
        
# Turn required pin on
def pin_on(i):
    global __pins
    if __pins[i-1] == 1:
        print("pin already high")
    else:
        __pins[i-1] = 1;
        __sendRegistry()
        
def all_pins_off():
    global pins
    __pins = [0,0,0,0,0,0,0,0]
    __sendRegistry()
        
def __shift(i):
    global __sck
    for y in range(i):
        __IO.output(__sck,1)  # sck high to shift the bits
        __IO.output(__sck,0)
        
def __send():
    global __rck
    __IO.output(__rck,1)  # rck high to send the output
    __IO.output(__rck,0)  # rck low to stop the output
    
    
def __shiftRegistry(condition, pin):
    global __pins
    tempPins = __pins [:]
    for i in range(7):
        __pins [i+1] = tempPins[i]
    __pins[pin] = condition
    
def __sendRegistry():
    global __pins, __ser
    for y in reversed(range(8)):
        if __pins[y] == 1:
            __IO.output(__ser,1)
        else:
            __IO.output(__ser,0)
        __shift(1)
    __send()
        
