def RR(AT,BT,TQ):
    l = len(AT)
    CT = [0]*l
    if BT[0] <= TQ:
        CT[0] = BT[0]
    BTC = []
    for i in BT:
        BTC.append(i)
    ATC = []
    for i in AT:
        ATC.append(i)
    comp = 0
    t = 0
    i = 0
    prev_index = -1
    prev_val = -1
    while(comp != l):
        AV = []
        j = 0
        if (len(ATC) != 0):
            while (ATC[j] <= t ):
                if(prev_val == -1 or ATC[j] != prev_val):
                    AV.append(j)
                    print('append' , ATC[j])
                print('ATC :', ATC, 'j:', j, 't:', t, 'AV:', AV)
                j += 1
                if (j == len(ATC)):
                    break
        if(len(AV) != 0):
            i = AV[0]
            if(BTC[i] >= TQ):
                BTC[i] = BTC[i] - TQ
                t += TQ + -1
            if(BTC[i] < TQ):
                t += BTC[i] -1
                BTC[i] = 0
            print("scheduling ",AT.index(ATC[i])+1)
            prev_index = AT.index(ATC[i])
            prev_val = ATC[i]
            if(BTC[i] == 0):
                print("removing ",ATC[i])
                CT[AT.index(ATC[i])] = t + 1
                ATC.remove(ATC[i])
                comp += 1
        t += 1
        print('CT : ',CT,ATC,BTC)
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

def RR_SA(AT,BT,TQ):
    l = len(AT)
    CT = [0]*l
    BTC = []
    for i in BT:
        BTC.append(i)
    ATC = []
    for i in AT:
        ATC.append(i)
    comp = 0
    t = 0
    #k = 0
    Q = []
    while(comp != l):
        AV = []
        j = 0
        if (len(ATC) != 0):
            while (ATC[j] <= t ):
                AV.append(j)
                Q.append(j)
                #print('append' , ATC[j])
                #print('ATC :', ATC, 'j:', j, 't:', t, 'AV:', AV)
                j += 1
                if (j == len(ATC)):
                    break
        if(len(AV) != 0):
            i = Q[0]
            print('Q : ',Q)
            if(BTC[i] >= TQ):
                BTC[i] = BTC[i] - TQ
                t += TQ + -1
            if(BTC[i] < TQ):
                t += BTC[i] -1
                BTC[i] = 0
            #print("scheduling ",AT.index(ATC[i])+1)
            prev_index = AT.index(ATC[i])
            prev_val = ATC[i]
            if(BTC[i] == 0):
                print("removing ",ATC[i])
                CT[AT.index(ATC[i])] = t + 1
                ATC.remove(ATC[i])
                comp += 1
        t += 1
        print('T :',t)
        Q.pop()
        print('CT : ',CT,ATC,BTC)
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

def RR_Easy(AT,BT,TQ):
    t =0
    flag = True
    l = len(AT)
    CT = [0]*l
    BTC = []
    for i in BT:
        BTC.append(i)
    comp = 0
    Q = []
    for i in AT:
        Q.append(i)
    while(comp != l):
        Now = Q.pop(0)
        if(BTC[AT.index(Now)] >= TQ):
            t+=TQ
            BTC[AT.index(Now)] -= TQ
            flag = False
        else:
            t+= BTC[AT.index(Now)]
            BTC[AT.index(Now)] = 0
            flag = False
        if BTC[AT.index(Now)] == 0:
            comp +=1
            CT[AT.index(Now)] = t
        else:
            Q.append(Now)
        if flag == True:
            t+=1
        flag = True
        #print('t',t,'CT : ',CT,'Q :',Q, BTC)
    TAT = [0] * len(AT)
    for i in range(len(AT)):
        TAT[i] = CT[i] - AT[i]
    WT = [0] * len(AT)
    for i in range(len(AT)):
        #WT[i] = TAT[i] - BT[i]
        WT[i] = CT[i] - BT[i]
    print('Pid\t\tAT\t\tBT\t\tCT\t\tTAT\t\tWT')
    for i in range(len(AT)):
        print(i + 1, '\t\t', AT[i], '\t\t', BT[i], '\t\t', CT[i], '\t\t', TAT[i], '\t\t', WT[i])
    print('Avg TAT : ', sum(TAT) / len(TAT), '\nAvg WT : ', sum(WT) / len(WT))

if __name__ == '__main__':
    #AT = [0,1,2,5,6]
    #BT = [2,2,3,1,4]
    #AT = [0,1,2,3,4,6]
    #BT = [4,5,2,1,6,3]
    #AT = [0,1,2,3]
    #BT = [5,4,2,1]
    AT = [0,1,2]
    BT = [24,3,3]
    TQ = 4
    RR_Easy(AT,BT,TQ)
