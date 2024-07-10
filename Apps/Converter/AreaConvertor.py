# Area => mm2 , cm2, dc2 , m2 ,km2 , Acre2 , Hect2 || Foot(ft2) , Mile (Mi2) , Yard (yd2), Inch (in2)

areaopr = ['mm²','cm²','dm²','m²','km²','Acre','ft²','mi²','yd²','in²','Hect']
AreaoprFull = [' Millimetre Square(mm²)',' Centimetre Square(cm²)',' Decimetre Square(dm²) ',' Metre Square (m²)',' Kilometre Square(km²) ',' Acre(Ac) ',' Square Foot(ft²) ',' Square Mile(mi²) ',' Square Yard(yd²) ',' Square Inch (in²)',' Hectare(ha) '] 
def con2m2(x,v):
    #mm =1,cm =2 ,dc =3 , m=4, km=5,Acre = 6,foot = 7 , Mile =8 , yard = 9 , inch =10 ,11.Hect
    if v == 1 :
        return x*0.000001
    if v == 2 :
        return x*0.0001
    if v == 3 :
        return x*0.01
    if v == 4 :
        return x*1.0
    if v == 5 :
        return x*1000000.0
    if v == 6 :
        return x*4046.944556
    if v == 7 :
        return x*0.0929030
    if v == 8 :
        return x*2590002.59
    if v == 9 :
        return x*0.83612739
    if v == 10 :
        return x*0.00064516
    if v == 11 :
        return x*10000

def con2mm2(m):
    return m*1000000.0
def con2cm2(m):
    return m*10000.0
def con2dm2(m):
    return m*100.0
def con2km2(m):
    return m*0.000001
def con2acre(m):
    return m*0.0002471
def con2Hec(m):
    return m*0.0001
def con2mi2(m):
    return m*0.0000003861
def con2yd2(m):
    return m*1.19599
def con2in2(m):
    return m*1550.0031
def con2ft2(m):
    return m*10.7639104

def RunAreaConvertor():
    AreaRun = True
    while AreaRun :
        print("\nAreal Operations Menu :\n")
        for i in range(len(AreaoprFull)):
            if i%2 == 0 :
                print("\t",i+1,".",AreaoprFull[i],end = "\t\t")
            else:
                print("\t",i+1,".",AreaoprFull[i])
        print("\n")
        #print("Values : \n\t1.mm2\t\t2.cm2\t\n\t3.dm2\t\t4.m2\t\n\t5.km2\t\t6.Area\t\n\t7.foot2\t\t8.mile2\t\n\t9.yard2\t\t10.inch2\t\n\t11.Hect\n")
        try:
            fro = int(input("Convert From : "))
            to = int(input("Convert To : "))
            Val = float(input("Value to Convert "+areaopr[fro-1]+' to '+areaopr[to-1]+' : '))
            m = con2m2(Val,fro)
            if to == 1 :
                result = con2mm2(m)
            elif to == 2 :
                result = con2cm2(m)
            elif to == 3 :
                result = con2dm2(m)
            elif to == 4 :
                result = m
            elif to == 5 :
                result = con2km2(m)
            elif to == 6 :
                result = con2area(m)
            elif to == 7 :
                result = con2ft2(m)
            elif to == 8 :
                result = con2mi2(m)
            elif to == 9 :
                result = con2yd2(m)
            elif to == 10 :
                result = con2in2(m)
            elif to == 11 :
                result = con2Hec(m)
            else :
                print("\n Inavlid Operation Request \n\tPlease Select an Option From Menu")
                break
            print("Convertion of "+str(Val)+" from "+areaopr[fro-1]+' to '+areaopr[to-1]+' : '+str(result))
            print("\n\t"+str(Val)+AreaoprFull[fro-1]+" = "+ str(result) +AreaoprFull[to-1]+"\n")
            z = input("Want to check again ? (Y/N)")
            if (z == 'Y') or (z == 'y'):
                AreaRun = True
            else:
                AreaRun = False
        except ValueError :
            print("Invalid Input Please Enter a Integer")
        except IndexError:
            print('\n\tPlease Select an Interger with in The Menu\n')
    
