import RPi.GPIO as IO   
import time             
IO.setwarnings(False)  

class shift_reg:
    
    __ser = 4
    __sck = 5
    __rck = 6
    
    IO.setmode(IO.BCM)      
    IO.setup(__ser,IO.OUT)      # pin 4 as output (SER)
    IO.setup(__sck,IO.OUT)      # pin 5 as output (SCK)
    IO.setup(__rck,IO.OUT)      # pin 6 as output (RCK)
    
    __pins = [0,0,0,0,0,0,0,0]


    def pinOnInRow(i, t=0.1):
        pinsAllOff()
        global __ser, __sck, __rck
        for y in range(i):    
            __shiftRegistry(1,0)
            IO.output(__ser,1)  # send a 1 to seriell input 
            time.sleep(t)     
            IO.output(__sck,1)  # sck high to shift the bits
            time.sleep(t)     
            IO.output(__sck,0)  
            IO.output(__ser,0)  
            IO.output(__rck,1)  # rck high to send the output
            time.sleep(t)     
            IO.output(__rck,0)  # rck low to stop the output
            

    def pinOffInRow(i, t=0.1):
        global __ser, __sck, __rck
        for y in range(i):    
            __shiftRegistry(0,0)
            IO.output(__ser,0)    # send a 0 to seriell input
            time.sleep(t)     
            IO.output(__sck,1)    # sck high to shift the bits
            time.sleep(t)     
            IO.output(__sck,0)    
            IO.output(__ser,0)    
            IO.output(__rck,1)    # rck high to send the output
            time.sleep(t)     
            IO.output(__rck,0)    # rck low to stop the output

         
    def pinsOnBin(i):
        global __pins
        for y in reversed(range(8)):
            __pins [y] = i%2
            i = i//2
        __sendRegistry()
            
    # Turn required pin on
    def pinOnAt(i):
        global __pins
        if __pins[i-1] == 1:
            print("pin already high")
        else:
            __pins[i-1] = 1;
            __sendRegistry()
            
    def pinsAllOff():
        global pins
        __pins = [0,0,0,0,0,0,0,0]
        __sendRegistry()
            
    def __shift(i):
        global __sck
        for y in range(i):
            IO.output(__sck,1)  # sck high to shift the bits
            IO.output(__sck,0)
            
    def __send():
        global __rck
        IO.output(__rck,1)  # rck high to send the output
        IO.output(__rck,0)  # rck low to stop the output
        
        
    def __shiftRegistry(condition, pin):
        global __pins
        tempPins = pins [:]
        for i in range(7):
            __pins [i+1] = tempPins[i]
        __pins[pin] = condition
        
    def __sendRegistry():
        global __pins, __ser
        for y in reversed(range(8)):
            if __pins[y] == 1:
                IO.output(__ser,1)
            else:
                IO.output(__ser,0)
            __shift(1)
        __send()
            
