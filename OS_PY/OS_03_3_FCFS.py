def FCFS(AT, BT):
    CT = [0] * len(AT)
    CT[0] = BT[0]
    i = 1
    while (i < len(AT)):
        CT[i] = CT[i - 1] + BT[i]
        i += 1
    TAT = [0] * len(AT)
    for i in range(len(AT)):
        TAT[i] = CT[i] - AT[i]
    WT = [0] * len(AT)
    for i in range(len(AT)):
        WT[i] = TAT[i] - BT[i]
    print('Pid\t\tAT\t\tBT\t\tCT\t\tTAT\t\tWT')
    for i in range(len(AT)):
        print(i + 1, '\t\t', AT[i], '\t\t', BT[i], '\t\t', CT[i], '\t\t', TAT[i], '\t\t', WT[i])
    print('Avg TAT : ', sum(TAT) / len(TAT), '\nAvg WT : ', sum(WT) / len(WT))

if __name__ == '__main__':
    AT = [0, 1, 2, 3, 4]
    BT = [4, 3, 1, 2, 5]
    FCFS(AT,BT)
