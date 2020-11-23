# Morse Code Generator and decoder

MC = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..',' ','']
AP = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','']

def A2M(string):
    k=[]
    mco = ''
    string = string.upper()
    listi = list(string)
    print(listi)
    for l in listi:
        for j in range(26):
            if AP[j] == l :
                k.append(j)
                break
            elif l == ' ':
                k.append(26)
                break
    for m in range(len(listi)):
        mco += str(MC[k[int(m)]]) + ' '
    return mco

def M2A(code):
    k=[]
    apo = []
    listc = code.split(' ')
    for l in listc:
        for j in range(26):
            if l == '-1':
                k.append(' ')
                break
            elif l == '-2':
                k.append('\n')
                break
            elif MC[j] == l :
                k.append(str(AP[j]))
                break
    apo = ''.join(k)
    return apo
    

RunMain = True
while RunMain:
    which = 0
    cont = 'n'
    which = input("\nPress 1 to Convert Morse Code to Alphabetic \nPress 2 to Convert Morse Code to Alphabetic\nAnything else to exit : ")
    RunMain = False
    Run = True 
    while Run:
        if int(which) == 1:
            i = input('String : ')
            print('Morse Code : '+ A2M(i))
        elif int(which) == 2:
            i = input('Write in dots(.) and dashes(-)\nfor every letter give space\nfor every word give Number -1 (for Space)\nfor enter give -2 \n\tEnter Morse Code: ' )
            print('String : '+ M2A(i))
        
        if int(which) == 1 or int(which) == 2:
            cont = input("Press Y to Check Again or M to goto to Main Menu : ")

        if cont == 'Y' or cont =='y':
            Run = True
        elif cont == 'M' or cont =='m':
            RunMain = True
            Run = False
        else:
            Run =False
            RunMain = False
