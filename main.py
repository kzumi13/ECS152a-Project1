from queue import *
import Random

#3.3 Arrival process the event   
def procArrEvent(my_event, cur_time, q_len):
    my_event
    #set the current time to the event time
    #process the arrival event
    
class Event():
    #event time
    #type
    #next event
    #prev event
    def __init__(self, event_time, event_type, event_n_event, event_p_event):
        self.time = event_time
        self.type = event_type #0 indicates arrival, 1 indicates departure
        self.n_event = event_n_event
        self.p_event = event_p_event
    

def main():
#3.2 INITIALIZATION
    MAXBUFFER = 10  #MAXBUFFER is abitrary.... apparently
    fifoQ = Queue(maxsize= MAXBUFFER) #initialize the queue
    

    #initialize the GEL
    #Python list will act as our linked list
    gel = []

    s_rate = 0 #service rate
    a_rate = 0 #arrival rate

    init_event = Event(0,0,None,None) #first event = arrival
    fifoQ.put(init_event)
    
    #for i in range(0, 100000):
        #get the first event from the GEL
        #if the event is an arrival, the process-arrival-event
        #Otherwise it must be a departure event and hence process-service-completion

    #output statistics
    if fifoQ.empty() == False:
        print(fifoQ.get())
    print(gel)

main()
