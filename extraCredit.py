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


def do_everything(aRate, dRate, maxBuff):
#3.2 INITIALIZATION
    cur_time = 0 #the current time
    MAXBUFFER = maxBuff  #MAXBUFFER is abitrary.... apparently
    #TODO: DO WE EVEN USE THE QUEUE?! IF SO WHAT WILL IT HOLD <-----------------------------------
    #fifoQ = queue.Queue(maxsize= MAXBUFFER) #initialize the queue
    fifoQ = []
    
    length = 0 #queue length
     
    
    #initialize the GEL
    #Python list will act as our linked list
    gel = []

    a_rate = aRate #arrival rate
    d_rate = dRate #service rate

    init_event = Event(cur_time + nedTime(a_rate),0,nedTime(d_rate)) #first event = arrival
    gel.append(init_event)
#ENDOF 3.2

#3.5 UTILIZATION <---------------------------------------NOT DONE AT ALL!
    #getting UTILIZATION
    util = 0 #utilization
    busy_start = 0
    busy_stop = 0
    busy_total = 0 #total amount of busy time
    total_t = 0 # the total time of sim

    #getting mean queue length
    mql = 0 #mean queue length NOT CURRENTLY USED FOR ANYTHING
    mqlsum = 0
    prev_ctime = 0 #previous current time

    #num packets dropped
    npd = 0 #number of packets dropped
#ENDOF 3.5
    
    #Begin FOR
    for i in range(0, 100000):
        #get the first event from the GEL
        cur_event = gel.pop(0)
#3.3    PROCESS THE ARRIVAL EVENT
        if cur_event.type == 0:
        
        #set the event time to the current event time
            cur_time = cur_event.time
            #1)generate the next arrival event
            ar_time = cur_time + nedTime(a_rate)
            #2)create a new packet with serivce
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
                dep_time = cur_time + service_t
                fifoQ.append(dep_time) #add service time to queue
                #print("+1! len = {len} curt = {cur} dep = {dep}" .format(len = length, cur = cur_time, dep = dep_time))
                #3)insert the departure event into the GEL
                new_devent = Event(dep_time, 1, 0) 
                gel.append(new_devent)
                gel.sort(key=lambda x: x.time) #sort based on the event time
                #UPDATE STATISTICS <---------------------------------------------------------
                busy_start = cur_time

            #)b there is something in the queue
            elif length-1 < MAXBUFFER:
                length = length + 1
                prev_dtime = fifoQ[length-2] #previous departure time
                fifoQ.append(service_t + prev_dtime) #add service time to queue
                #print("+1 len = {len} curt = {cur} dept = {dep}" .format(len = length, cur = cur_time, dep = service_t + prev_dtime))
            #Queue is full and will drop the packet
            else:
                #drop the packet!!!!
                npd = npd + 1
#ENDOF 3.36

#3.4    PROCESS THE DEPARTURE EVENT
        elif cur_event.type == 1:
            #set the curent time to the event time
            cur_time = cur_event.time
            #UDATE THE SATISTICS!??! <-----------------------------------------------
            length = length - 1
            fifoQ.pop(0) #remove the packet
            #print("-1 len = {len} ctime = {cur}" .format(len = length, cur = cur_time))
            #if the queue is empty DO NOTHING
            #else, if there is something in the queue
            if length > 0:
                #create a departure event for time
                next_dtime = fifoQ[0] #departure time of next packet in queue
                new_devent = Event(next_dtime, 1, service_t)
                #insert event into GEL
                gel.append(new_devent)
                gel.sort(key=lambda x: x.time) #sort based on the event time
            else:
#3.5 do some statistics work
                busy_stop = cur_time
                busy_total = busy_total + busy_stop - busy_start
                
        mqlsum = mqlsum + ((cur_event.time - prev_ctime) * length)
        total_t = cur_event.time
        prev_ctime = total_t
        
#ENDOF 3.4
    #return answer
    print("b/t = {bt} mql = {mql} npd = {npd}" .format(bt = busy_total/total_t, mql = mqlsum/total_t, npd = npd))
    util = busy_total/total_t
    mql = mqlsum/total_t
    return util, mql, npd

#3.7 Phase 1 Experiments
def main():
    u_list = []
    mql_list = []
    npd_list = []

    #1)
    print("Part 1")
    for i in [.1,.25,.4,.55,.65,.8,.9]:
        util, mql, npd = do_everything(i, 1, 99999)
        u_list.append(util)
        mql_list.append(mql)
        npd_list.append(npd)
    u_list = []
    mql_list = []
    npd_list = []
    
    #3)
    print("Part 3")
    for i in [1, 20, 50]:
        for j in [.2,.4,.6,.8,.9]: 
            util, mql, npd = do_everything(j, 1, i)
            u_list.append(util)
            mql_list.append(mql)
            npd_list.append(npd)
        u_list = []
        mql_list = []
        npd_list = []

    
    
main()
