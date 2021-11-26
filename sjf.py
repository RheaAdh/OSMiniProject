def SJF(bursttime, x):  # x is unsorted list
    print("Process    BurstTime    WaitingTime    TurnaroundTime")
    i = 0
    waiting_time = 0
    turnaround_time = 0
    empty1 = []
    empty2 = []
    while(i < len(bursttime)):
        turnaround_time += bursttime[i]
        print("P" + str(x.index(bursttime[i])+1),str(bursttime[i]),str(waiting_time),str(turnaround_time), sep='\t\t')
        x[x.index(bursttime[i])] = -1
        empty1.append(waiting_time)
        empty2.append(turnaround_time)
        waiting_time += bursttime[i]
        i += 1
    return(empty1, empty2)


np = int(input("Enter the number of processes: "))
burst_times = []
for i in range(np):
    burst_times.append(
        int(input("Enter the burst times for the processes "+str(i+1)+":")))
lis = SJF(sorted(burst_times), burst_times)
print("Average waiting time: "+str(sum(lis[0])/len(lis[0])))
print("Average waiting time: "+str(sum(lis[1])/len(lis[1])))
