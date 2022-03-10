print("\n\n\n\n\t\t\t\tWelcome to \" F L A M E S \" \n\n\n")
run = True
while run:
    n1 = input("Enter First Name : ")
    n2= input("Enter Second Name : ")
    result=True
    count = 0
    total=0
    flame = ['F','L','A','M','E','S']
    flames = ['F','L','A','M','E','S']
    flameval = {'F':'Friend','L':'Love','A':'Affection','M':'Mariage','E':'Enemy','S':'Sibling'}
    m1 = list(n1)
    m2 = list(n2)

    if len(m1) >= len(m2):
        k1 = m1
        k2 = m2
    elif len(m2) > len(m1):
        k1 = m2
        k2 = m1 
    for i in range(len(k1)):    
        for j in range(len(k2)):
            if k1[i] == k2[j]:
                k1[i]=0
                k2[j]=0
                count += 1
                break
    
    def mylen(givenList):
        stronly = 0
        for i in range(len(givenList)):
            if givenList[i] != 0 :
                stronly +=1
        return stronly
    total = mylen(k1) + mylen(k2)
    #method 1
    while (len(flame)!=1):    
        c = total % len(flame)
        flame.pop(c)
    #method 2
    see = -1
    new = []
    for i in range(len(flames)):
        print(str(flames[i]),end=' ')
    print('\n')
    while mylen(flames) != 1:
        for i in range(len(flames)):   
            see +=1
            if see == (total-1):
                #flames[i] = 0
                #flames.pop(i)
                new.append(i)
                see = -1
            
        for i in range(len(new)-1,-1,-1):
            flames.pop(new[i])
            for i in range(len(flames)):
                print(str(flames[i]),end=' ')
            print('\n')
        new = []
    
    
    print("THE OFFICIAL AND MOST TRUSTED WAY :\n\n\t\tgiven that ",n2," is ",flameval[flames[0]],"To ",n1)
    print("\n\nALSO POSSIBLE CALCULATION SHOWS:\n\n\t\tthat ",n2," is ",flameval[flame[0]],"To ",n1)
    z=input("\n\nEnter y to check again : ")
    if z != 'y':
        run = False
