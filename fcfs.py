def findWaitingTimeForAllProcesses(processes, n, bt, wait):
    wait[0] = 0
    for i in range(1, n):
        wait[i] = bt[i - 1] + wait[i - 1]


def findTurnAroundTimeForAllProcesses(processes, n, bt, wait, tat):
    for i in range(n):
        tat[i] = bt[i] + wait[i]


def findAverageTime(processes, n, bt):
    fcfsOutput = []
    wait = [0] * n
    tat = [0] * n
    totalWaitingTime = 0
    total_tat = 0
    findWaitingTimeForAllProcesses(processes, n, bt, wait)
    findTurnAroundTimeForAllProcesses(processes, n, bt, wait, tat)

    for i in range(n):
        burstData = str(bt[i])
        waitData = str(wait[i])
        tatData = str(tat[i])
        totalWaitingTime = totalWaitingTime + wait[i]
        total_tat = total_tat + tat[i]

        fcfsOutput.append(
            {"process": str(i+1), "burstTime": burstData, "waitingTime": waitData, "turnAroundTime": tatData})

    avgwait = round(totalWaitingTime / n, 5)
    avgturn = round(total_tat / n, 5)
    return fcfsOutput, str(avgwait), str(avgturn)
