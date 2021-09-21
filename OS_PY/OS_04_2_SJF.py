def SJF(AT,BT):
    CT = [0]*len(AT)
    CT[0] = BT[0]
    ATC = []
    for i in AT:
        ATC.append(i)
    i = 1
    comp = 0
    t = 0
    while(comp != 5):
        AV = []
        j = 0
        if(len(ATC) !=0 ):
            while (ATC[j] <= t):
                AV.append(j)
                j += 1
                if (j == len(ATC)):
                    break
        m = 0
        for k in AV:
            print(BT[AT.index(ATC[k])],BT[AT.index(ATC[m])])
            if BT[AT.index(ATC[k])] < BT[AT.index(ATC[m])]:
                m = k
            print(BT[AT.index(ATC[m])] + t)
        if(len(AV) != 0):
            print(CT)
            print(AV[m],ATC[AV[m]],AT[ATC[AV[m]]],BT[AT[ATC[AV[m]]]])
            CT[AT.index(ATC[m])] = BT[AT[ATC[AV[m]]]] + t
            ATC.remove(ATC[m])
            comp += 1
            t = t + BT[m] - 1
        t += 1
    TAT = [0]*len(AT)
    for i in range(len(AT)):
        TAT[i] = CT[i] - AT[i]
    WT = [0] * len(AT)
    for i in range(len(AT)):
        WT[i] = TAT[i] - BT[i]
    print('Pid\t\tAT\t\tBT\t\tCT\t\tTAT\t\tWT')
    for i in range(len(AT)):
        print(i+1,'\t\t',AT[i],'\t\t',BT[i],'\t\t',CT[i],'\t\t',TAT[i],'\t\t',WT[i])
    print('Avg TAT : ',sum(TAT)/len(TAT),'\nAvg WT : ',sum(WT)/len(WT))

if __name__ == '__main__':
    AT = [0, 1, 2, 3, 4]
    BT = [4, 3, 1, 2, 5]
    SJF(AT, BT)
