print("============================   WELCOME TO ROCK-PAPER-SCISSOR GAME  ============================")
print("Rules:\n\tThis game Consists of three objects namely\n\t\t1.ROCK\n\t\t2.PAPER\n\t\t3.SCISSOR\n\tUser should choose a number 1/2/3 for ROCK/PAPER/SCISSOR")
print("\tEach round has a winner by considering\n\t\tPAPER TAKES ROCK  \n\t\tROCK TAKES SCISSOR \n\t\tSCISSOR TAKES PAPER ")
print("\tif any of the players gets 5 points then he must be considered as \'WINNER\'")
print("\tHere the Second player is Computer")
z='y'
while(z=='y' or z=='Y'):
    u1=0
    c1=0
    while((u1!=5) and (c1!=5)):    
        val=int(input("Select a number :"))
        if val in range(1,4):
            dic={1:'rock',2:'paper',3:'scissor'}
            user=dic[val]
            import random
            comp=random.randint(0,2)
            game=['rock','paper','scissor']
            if(user==game[comp]):
                print("\n\t\t\t\t\tNO POINTS - BOTH ARE SAME\n")
            elif(val==1):
                if(comp==1):
                    print("\nYOU LOOSE - COMPUTER WON THIS ROUND")
                    print("------  PAPER TAKES ROCK   ------")
                    c1+=1
                elif(comp==2):
                    print("\nYOU WON - COMPUTER LOOSE THIS ROUND")
                    print("------  ROCK TAKES SCISSOR   ------")
                    u1+=1
            elif(val==2):
                if(comp==0):
                    print("\nYOU WON - COMPUTER LOOSE THIS ROUND")
                    print("------  PAPER TAKES ROCK   ------")
                    u1+=1
                elif(comp==2):
                    print("\nYOU LOOSE - COMPUTER WON THIS ROUND")
                    print("------  SCISSOR TAKES PAPER   ------")
                    c1+=1
            elif(val==3):
                if(comp==0):
                    print("\nYOU LOOSE - COMPUTER WON THIS ROUND")
                    print("------  ROCK TAKES SCISSOR   ------")
    
                    c1+=1
                elif(comp==1):
                    print("\nYOU WON - COMPUTER LOOSE THIS ROUND")
                    print("------  SCISSOR TAKES PAPER   ------")
                    u1+=1
            print('Yours :'+user+'\t\t\tComputers :'+game[comp])
            print('Points:'+str(u1)+'\t\t\tPoints:'+str(c1))
        else:
            print("\n\n------------> INVALID INPUT\n\n")
    if(u1==5):
        print("\   /  / \  |   |    |    | ----- |\   |")
        print(" \ /  |   | |   |    |    |   |   | \  |")
        print("  |   |   | |   |    | /\ |   |   |  \ |") 
        print("  |    \ /   \_/     \/  \/ ----- |   \|")
    else:
        print("\   /  / \  |   |    |     / \  \--- |--- |---")
        print(" \ /  |   | |   |    |    |   |  \   |__  |__")
        print("  |   |   | |   |    |    |   |   \  |    |   ") 
        print("  |    \ /   \_/     |___  \ /  ---\ |--- |---")
    z=input("PRESS Y TO PLAY AGAIN OR ANY KEY ELSE TO EXIT :")
    if ((z!='y') and (z!='Y')):
        print("\n\n\n\t\t\t\t\t\t\t BYE...\n")
