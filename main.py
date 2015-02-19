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
    #TODO: DO WE EVEN USE THE QUEUE?! IF SO WHAT WILL IT HOLD <-----------------------------------
    fifoQ = queue.Queue(maxsize= MAXBUFFER) #initialize the queue
    length = 0 #queue length
     
    
    #initialize the GEL
    #Python list will act as our linked list
    gel = []

    a_rate = .5 #arrival rate
    d_rate = .5 #service rate

    init_event = Event(cur_time + nedTime(a_rate),0,nedTime(d_rate)) #first event = arrival
    gel.append(init_event)
#ENDOF 3.2

#3.5 UTILIZATION <---------------------------------------NOT DONE AT ALL!
    util = 0 #utilization
    mql = 0 #mean queue length
    npd = 0 #number of packets dropped
#ENDOF 3.5
   #Begin FOR
    for i in range(0, 10):
        #get the first event from the GEL
        gel.reverse()
        cur_event = gel.pop()
        gel.reverse()

#3.3    PROCESS THE ARRIVAL EVENT
        if cur_event.type == 0:
        #set the event time to the current event time
            cur_time = cur_event.time
            #1)generate the next arrival event
            ar_time = cur_time + nedTime(a_rate)
            #2)TODO create a new packet with serivce <--------------------------- THIS ONE STILL NEEDS WORK!?!?!? I DONT UNDERSTAND!!!!
            service_t = nedTime(d_rate)
            #3)create a new arrival event
            new_aevent = Event(ar_time, 0, service_t)
            #4)Insert the event into the list
            gel.append(new_aevent)
            gel.sort(key=lambda x: x.time) #sort based on the event time

        #process the arrival event
            #a)if server is free, schedule for transmission
            if length == 0:
            #if fifoQ.qsize() == 0:
                #1,2)get the service time of the packet. Create a departure event with time = curtime+transtime
                length = length + 1 #add packet to the queue
                fifoQ.put(service_t) #add service time to queue
                dep_time = cur_time + service_t
                #3)insert the departure event into the GEL
                new_devent = Event(dep_time, 1, 0) 
                gel.append(new_devent)
                gel.sort(key=lambda x: x.time) #sort based on the event time
                #UPDATE STATISTICS <---------------------------------------------------------

            #)b there is something in the queue
            elif length-1 < MAXBUFFER:
                lenght = length + 1
                fifoQ.put(service_t) #add service time to queue
            #Queue is full and will drop the packet
            else:
                #drop the packet!!!!
                npd = npd + 1
#ENDOF 3.3

#3.4    PROCESS THE DEPARTURE EVENT
        elif cur_event.type == 1:
            #set the curent time to the event time
            cur_time = cur_event.time
            #UDATE THE SATISTICS!??! <-----------------------------------------------
            length = length - 1
            fifoQ.get()
            #if the queue is empty DO NOTHING
            #else, if there is something in the queue
            if length > 0:
                #create a departure event for time
                service_t = fifoQ.get() #<-------- we cannot use a queue since we only what to look at it, and not pop it off
                new_devent = Event(cur_time + service_t, 1, service_t)
                #insert event into GEL
                gel.append(new_devent)
                gel.sort(key=lambda x: x.time) #sort based on the event time
#ENDOF 3.4

    #END FOR
    
    #output statistics
    #if fifoQ.empty() == False:
    #    print(fifoQ.get())
    #print(gel)

    for events in gel:
        print(events.time,  events.service_t)
    
    mylist = [0,1,2,3,4,5]
    print(mylist[1]);

main()
