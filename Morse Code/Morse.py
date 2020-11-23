# Morse Code Generator and decoder

MC = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
AP = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
k=-1
Run = True
while Run:
    i = input('Alphabet : ')
    i = i.upper()
    for j in range(26):
        if AP[j] == i :
            k = j
            break    
    print('Morse Code for ',i, ' is ',MC[k])
    cont = input("Press Y to Check Again")
    Run =False
    if cont == 'Y' or cont =='y':
        Run = True
        
