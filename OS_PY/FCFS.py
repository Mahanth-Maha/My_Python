def FCFS(AT, BT):
    """Criteria AT - Non Preemptive"""
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

'''
def SJF(AT, BT):
    """Criteria BT - Non Preemptive"""
    ATC = AT
    l = len(AT)
    CT = [0] * l
    i = 1
    t = 0
    comp = 0
    while (comp != l):
        AV = []
        j = 0
        while (ATC[j] <= t ):
            AV.append(j)
            #print('ATC :', ATC, 'j:', j, 't:', t, 'AV:', AV)
            j += 1
            if(j == len(ATC)):
                break
        m = 0
        mval = 0
        for k in AV:
            if AV[k] < AV[m] :
                m = k
                mval = AV[]
        if(len(AV) != 0):
            val = AV[m]
            print(val,CT,AV)
            CT[AT.index(val)] = BT[m] + t
            ATC.remove(ATC[m])
            comp += 1
            t = t + BT[m] - 1
        t += 1
    print(CT)
    TAT = [0] * l
    for i in range(l):
        TAT[i] = CT[i] - AT[i]
    WT = [0] * l
    for i in range(l):
        WT[i] = TAT[i] - BT[i]
    print('Pid\t\tAT\t\tBT\t\tCT\t\tTAT\t\tWT')
    for i in range(len(AT)):
        print(i + 1, '\t\t', AT[i], '\t\t', BT[i], '\t\t', CT[i], '\t\t', TAT[i], '\t\t', WT[i])
    print('Avg TAT : ', sum(TAT) / len(TAT), '\nAvg WT : ', sum(WT) / len(WT))
'''

def SJF_SA(AT,BT):
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
                print('ATC :', ATC, 'j:', j, 't:', t, 'AV:', AV)
                j += 1
                if (j == len(ATC)):
                    break
        m = 0
        for k in AV:
            print(BT[AT.index(ATC[k])],BT[AT.index(ATC[m])])
            if BT[AT.index(ATC[k])] < BT[AT.index(ATC[m])]:
            #if AV[k] < AV[m]:
                m = k
            print(BT[AT.index(ATC[m])] + t)
            #print('HE ',BT[AT[ATC[AV[m]]]])
        if(len(AV) != 0):
            #val = AV[m]
            #print(val,CT,AV)
            print(CT)
            print(AV[m],ATC[AV[m]],AT[ATC[AV[m]]],BT[AT[ATC[AV[m]]]])
            CT[AT.index(ATC[m])] = BT[AT[ATC[AV[m]]]] + t
            #CT[AT.index(ATC[m])] = BT[AT.index(ATC[m])] + t
            ATC.remove(ATC[m])
            comp += 1
            t = t + BT[m] - 1
        #print(comp,t)
        t += 1
    #print('CT : ',CT,AT)
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
    #FCFS FAil
    # AT = [0, 3, 5]
    # BT = [2, 1, 6]
    FCFS(AT,BT)
    #SJFS FAIL
    # AT = [ 1, 2, 3, 4,5]
    # BT = [ 7, 5, 1,2,8]
    SJF_SA(AT, BT)
