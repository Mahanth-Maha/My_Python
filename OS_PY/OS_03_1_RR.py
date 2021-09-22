def RR(AT,BT,TQ):
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
        if(BTC[AT.index(Now)] > TQ):
            t+=TQ
            BTC[AT.index(Now)] -= TQ
            print("P",AT.index(Now)+1,end = "\t")
            flag = False
            Q.append(Now)
        else:
            t+= BTC[AT.index(Now)]
            BTC[AT.index(Now)] = 0
            print("P",AT.index(Now)+1,end = "\t")
            flag = False
            comp +=1
            CT[AT.index(Now)] = t
        if flag == True:
            t+=1
        flag = True
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
    AT = [0,1,2]
    BT = [24,3,3]
    TQ = 4
    RR(AT,BT,TQ)
