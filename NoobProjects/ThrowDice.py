print("WELCOME")
z='y'
while(z=='y' or z=='Y'):
    import random
    x=random.randint(1,6)
    print("DICE ROLLED\n")
    if(x==1):
        print("╔─────────╗")
        print("|         |")
        print("|    ☻    |")
        print("|         |")
        print("╚─────────╝")
    if(x==2):
        print("╔─────────╗")
        print("|         |")
        print("|  ☻   ☻  |")
        print("|         |")
        print("╚─────────╝")
    if(x==3):
        print("╔─────────╗")
        print("| ☻       |")
        print("|    ☻    |")
        print("|       ☻ |")
        print("╚─────────╝")
    if(x==4):
        print("╔─────────╗")
        print("| ☻     ☻ |")
        print("|         |")
        print("| ☻     ☻ |")
        print("╚─────────╝")
    if(x==5):
        print("╔─────────╗")
        print("| ☻     ☻ |")
        print("|    ☻    |")
        print("| ☻     ☻ |")
        print("╚─────────╝")
        
    if(x==6):
        print("╔─────────╗")
        print("| ☻  ☻  ☻ |")
        print("|         |")
        print("| ☻  ☻  ☻ |")
        print("╚─────────╝")
    z=input("\n\n\nTO PLAY AGAIN PRESS Y : ")   
    if((z!='y') and z!='Y'):
        print('\n\n\n\t\t\t\tBYE...\n\n\n')
