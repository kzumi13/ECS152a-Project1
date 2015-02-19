import queue
import random
import math

#3.6 Generating Time Intervals in Negative Exponential Distribution
def nedTime(rate):
    u = random.random()
    return ((-1/rate) * math.log(1-u))
#ENDOF 3.6
    
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

def main():
#3.2 INITIALIZATION
    cur_time = 0 #the current time
    MAXBUFFER = 10  #MAXBUFFER is abitrary.... apparently
    fifoQ = queue.Queue(maxsize= MAXBUFFER) #initialize the queue
     
    
    #initialize the GEL
    #Python list will act as our linked list
    gel = []

    a_rate = .5 #arrival rate
    d_rate = .5 #service rate

    init_event = Event(cur_time + nedTime(a_rate),0,nedTime(d_rate)) #first event = arrival
    gel.append(init_event)
#ENDOF 3.2
    
    for i in range(0, 10):
        #get the first event from the GEL
        cur_event = gel[0]

#3.3    PROCESS THE ARRIVAL EVENT
        if cur_event.type == 0:
        #set the event time to the current event time
            cur_event.time = cur_time
            
            #1)generate the next arrival event
            ar_time = cur_time + nedTime(a_rate)
            #2)create a new packet with serivce <--------------------------- THIS ONE STILL NEEDS WORK!?!?!? I DONT UNDERSTAND!!!!
            service_t = nedTime(d_rate)
            #3)create a new arrival event
            new_event = Event(ar_time, 0, service_t)
            #4)Insert the event into the list
            gel.append(new_event)
            gel.sort(key=lambda x: x.event_time) #sort based on the event time

        #process the arrival event
            #a)if server is free, schedule for transmission
            if fifoQ.qsize() == 0:
                
#ENDOF 3.3
                
    #output statistics
    #if fifoQ.empty() == False:
    #    print(fifoQ.get())
    #print(gel)

    for events in gel:
        print(events.service_t)
    
    mylist = [0,1,2,3,4,5]
    print(mylist[1]);

main()
