import random
import queue
import math

class Event():
    #event time
    #type
    #next event
    #prev event
    def __init__(self, event_time, event_type, service_t): #event_n_event, event_p_event):
        self.time = event_time
        self.type = event_type #0 indicates arrival, 1 indicates departure
        self.service_t = service_t #service time of the event
        #self.n_event = event_n_event
        #self.p_event = event_p_event
        self.sender = NONE
        self.receiver = NONE

class Host():
    def __init__(self, ID):
        self.ID = ID
        self.status = 0 # 0 = idle , 1 = sending
        self.oldStatus = self.status # replicate the old status
        self.buffer = []
        self.count = -1
        self.wait= -1
        self.tries = 0
        self.queueDelay = 0
        self.transDelay = 0
        
def main():
    throughput = 0
    totalDelay = 0
    averageDelay = 0
    hostCount = 10  # part a N = 10
    a_rate = 0.1
    backoffT = 0.5
    totalTransmitted = 0
    hostBuffer = []  # will be use to store all 10 hosts
    cur_time = 0
    gel = []
 
    fifoQ = [] # buffer that have hosts for transmit
    busyFlag = 0
    
    length = 0 #queue length
     
    SIFS =   0.00005       #0.05 msec 
    DIFS =   0.0001       #0.1 msec
    SENSE =  0.00001       #0.01 msec
    FRAMESIZE = 64
    CHANNELCAP = 11   #channel transtmission
    MAXFRAMELENGTH = 1554  # data frame length
    
    #create each host using for loop
    for i in range(hostCount):  # we making 10 hosts first part
        hostBuffer.append(hostBuffer[i])  # and we stored it inside the hostBuffer, which contains all 10 hosts

    #create initial arrival event   
    init_event = Event(cur_time + nedTime(a_rate),0,nedTime(d_rate)) #first event = arrival = 0; departure = 1
    init_event.receiver = random.randint(0, hostCount -1)
    init_event.sender = random.randint(0, hostCount -1)
    gel.append(init_event)
    gel.sort(key=lambda x: x.time)

    #check
    while cur_time < 10000:
        cur_time = cur_time + 1
        for i in hostBuffer:
            if not busyFlag:  # so assume busyFlag is not equal to 0
                if host.counter == 0 and len(host.buffer) > 0:  # if the counter is 0 and buffer contains some files
                    fifoQ.append(host)
                    host.counter = -1 # reset it
                elif host.count > 0:
                    host.count = host.counter - 1 # keep decreasing till it reaches 0 so you can transmit files
            else:
                if host.wait > 0:
                    host.wait = host.wait - 1
                elif host.wait == 0:
                    fifoQ.append(host)
                    host.wait = -1
                

                    
                
