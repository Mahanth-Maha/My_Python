# Morse Code Generator and decoder

MC = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
AP = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

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
                print(AP[j])
                break
    for m in range(len(listi)):
        mco += str(MC[k[int(m)]]) + ' '

    return mco
    
Run = True
while Run:
    i = input('String : ')
    print('Morse Code '+A2M(i))
    
    cont = input("Press Y to Check Again")
    Run =False
    if cont == 'Y' or cont =='y':
        Run = True
        
