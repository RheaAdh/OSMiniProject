def findWaitingTimeForAllProcesses(processes, n, bt, wt, quantum):
    rem_bt = [0] * n

    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0

    while(1):
        done = True
        for i in range(n):
            if (rem_bt[i] > 0):
                done = False
                if (rem_bt[i] > quantum):
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0

        if (done == True):
            break


def findTurnAroundTimeForAllProcesses(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def findAverageTime(processes, n, bt, quantum):
    roundrobinOutput = []
    wt = [0] * n
    tat = [0] * n

    findWaitingTimeForAllProcesses(processes, n, bt, wt, quantum)
    findTurnAroundTimeForAllProcesses(processes, n, bt, wt, tat)

    # print("-----------------RR----------------")
    # print("Processes Burst Time	 Waiting", "Time Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):

        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        burstData = str(bt[i])
        waitData = str(wt[i])
        tatData = str(tat[i])
        # print(" ", i + 1, "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i])
        roundrobinOutput.append(
            {"process": str(i+1), "burstTime": burstData, "waitingTime": waitData, "turnAroundTime": tatData})

    # print("\nAverage waiting time = %.5f " % (total_wt / n))
    # print("Average turn around time = %.5f " % (total_tat / n))
    avgwait = round(total_wt / n, 5)
    avgturn = round(total_tat / n, 5)
    return roundrobinOutput, str(avgwait), str(avgturn)


if __name__ == "__main__":
    # Process id's
    proc = [1, 2, 3]  # Process IDs
    n = 3  # Number of processes

    burst_time = [10, 5, 8]  # Burst time of all processes

    quantum = 2  # We keep time quantum fixed at 2

    findAverageTime(proc, n, burst_time, quantum)
