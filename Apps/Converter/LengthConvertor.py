# Length => mm , cm , dc , m ,km , µm || Foot(ft) , Mile (Mi) , Yard (yd), Inch (in)

#Functions for Converting each of these into anothers
LenRun = False

def con2m(x,v):
    #mm =1,cm =2 ,dc =3 , m=4, km=5,µm = 6,foot = 7 , Mile =8 , yard = 9 , inch =10 
    if v == 1 :
        return x/1000.0
    if v == 2 :
        return x/100.0
    if v == 3 :
        return x/10.0
    if v == 4 :
        return x*1.0
    if v == 5 :
        return x*1000.0
    if v == 6 :
        return x*1000000.0
    if v == 7 :
        return x*0.30479999
    if v == 8 :
        return x*1609.26939169
    if v == 9 :
        return x*0.91439999
    if v == 10 :
        return x*0.02540000

def con2mm(m):
    return m*1000
def con2cm(m):
    return m*100
def con2dc(m):
    return m*10
def con2km(m):
    return m/1000
def con2macrom(m):
    return m/1000000
def con2ft(m):
    return m*3.2808399
def con2mi(m):
    return m*0.0006214
def con2yd(m):
    return m*1.0936133
def con2in(m):
    return m*39.3700787


def RunLengthConvertor():
    LenRun = True
    lenopr = ['mm','cm','dm','m','km','µm','ft','mi','yd','in']
    lenoprFull = [' Millimetre(mm) ',' Centimetre(cm) ',' Decimetre(dc) ',' Metre(m) ',' Kilometre(km) ',' Micrometre (µm) ',' Foot(ft) ',' Miles(mi) ',' Yard(yd) ',' Inch(in) ']
    while LenRun :
        print("\nLength Operations Menu :\n")
        for i in range(len(lenoprFull)):
            if i%2 == 0 :
                print("\t",i+1,".",lenoprFull[i],end = "\t\t")
            else:
                print("\t",i+1,".",lenoprFull[i])
        print("\n")
        #print("Values : \n\t1.mm\t\t2.cm\t\n\t3.dm\t\t4.m\t\n\t5.km\t\t6.µm\t\n\t7.foot\t\t8.mile\t\n\t9.yard\t\t10.inch\t\n\t")
        try:
            fro = int(input("Convert From : "))
            to = int(input("Convert To : "))
            Val = float(input("Value to Convert "+lenopr[fro-1]+' to '+lenopr[to-1]+' : '))
            m = con2m(Val,fro)
            if to == 1 :
                result = con2mm(m)
            elif to == 2 :
                result = con2cm(m)
            elif to == 3 :
                result = con2dm(m)
            elif to == 4 :
                result = m
            elif to == 5 :
                result = con2km(m)
            elif to == 6 :
                result = con2macrom(m)
            elif to == 7 :
                result = con2ft(m)
            elif to == 8 :
                result = con2mi(m)
            elif to == 9 :
                result = con2yd(m)
            elif to == 10 :
                result = con2in(m)
            else :
                print("\n Inavlid Operation Request \n\tPlease Select an Option From Menu")
                break
            print("Convertion of "+str(Val)+" from "+lenopr[fro-1]+' to '+lenopr[to-1]+' : '+str(result))
            print("\n\t"+str(Val)+lenoprFull[fro-1]+" = "+ str(result) +lenoprFull[to-1]+"\n")
            z = input("Want to check again ? (Y/N)")
            if (z == 'Y') or (z == 'y'):
                LenRun = True
            else:
                LenRun = False
        except ValueError :
            print("Invalid Input ! , Please Enter a Number")
        except IndexError:
            print('\n\tPlease Select an Interger with in The Menu\n')
