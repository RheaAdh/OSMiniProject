def findAverageTime(bursttime, x):  # x is unsorted list
    # print("--------------------SJF-------------------")
    # print("Process    BurstTime    WaitingTime    TurnaroundTime")
    i = 0
    waiting_time = 0
    turnaround_time = 0
    empty1 = []
    empty2 = []
    sjfOutput = list()

    while(i < len(bursttime)):
        turnaround_time += bursttime[i]

        sjfOutput.append({"process": x.index(
            bursttime[i])+1, "burstTime": bursttime[i], "waitingTime": waiting_time, "turnAroundTime": turnaround_time})

        # print("P" + str(x.index(bursttime[i])+1), str(bursttime[i]),
        #       str(waiting_time), str(turnaround_time), sep='\t\t')
        x[x.index(bursttime[i])] = -1
        empty1.append(waiting_time)
        empty2.append(turnaround_time)
        waiting_time += bursttime[i]
        i += 1

    # print("Average waiting time: "+str(sum(empty1)/len(empty1)))
    # print("Average turn around time: "+str(sum(empty2)/len(empty2)))
    return sjfOutput


if __name__ == '__main__':
    np = int(input("Enter the number of processes: "))
    burst_times = []

    for i in range(np):
        burst_times.append(
            int(input("Enter the burst times for the processes "+str(i+1)+":")))

    lis = findAverageTime(sorted(burst_times), burst_times)
