#Speed  => Speed of light , inch/s ,m/s , km/s , kmph ,mph
import LengthConvertor as lc

Spdopr = ['c','inch/s','m/s','km/s','Kmph','Mph',]
SpdoprFull = [' Speed of Light (c) ',' Inch per Second(inch/s) ',' Metre per Second(m/s) ',' Kilometre per Second(km/s)',' Kilometre per Hour(kmph) ',' Miles per Hour(mph) ']

def con2kmph(x,v):
    #c = 1 , inch/s =2 ,m/s =3, km/s = 4 , kmph =5 ,mph =6 
    if v == 1 :
        return x*1079266099.0526
    if v == 2 :
        k = lc.con2m(x,10)
        l = lc.con2km(k)*3600
        return l
    if v == 3 :
        return x*3.6
    if v == 4 :
        return x*3600
    if v == 5 :
        return x*1.0
    if v == 6 :
        k = lc.con2m(x,4)
        return lc.con2km(k)

def con2c(m):
    return m*0.0000000009265
def con2ins(m):
    k = lc.con2m(m,5)
    l = lc.con2in(k)/3600
    return l
def con2mps(m):
    return m/3.6
def con2kmps(m):
    return m*(1/3600)
def con2mph(m):
    k = lc.con2m(m,5)
    return lc.con2mi(k)


def RunSpdConvertor():
    SpdRun = True
    while SpdRun :
        print("\nSpeed Operations Menu :\n")
        for i in range(len(SpdoprFull)):
            if i%2 == 0 :
                print("\t",i+1,".",SpdoprFull[i],end = "\t\t")
            else:
                print("\t",i+1,".",SpdoprFull[i])
        print("\n")
        try:
            fro = int(input("Convert From : "))
            to = int(input("Convert To : "))
            Val = float(input("Value to Convert "+Spdopr[fro-1]+' to '+Spdopr[to-1]+' : '))
            m = con2kmph(Val,fro)
            #c = 1 , inch/s =2 ,m/s =3, km/s = 4 , kmph =5 ,mph =6 
            if to == 1 :
                result = con2c(m)
            elif to == 2 :
                result = con2ins(m)
            elif to == 3 :
                result = con2mps(m)
            elif to == 4 :
                result = con2kmps(m)
            elif to == 5 :
                result = m
            elif to == 6 :
                result = con2mph(m)
            else :
                print("\n Inavlid Operation Request \n\tPlease Select an Option From Menu")
                break
            print("Convertion of "+str(Val)+" from "+Spdopr[fro-1]+' to '+Spdopr[to-1]+' : '+str(result))
            print("\n\t"+str(Val)+SpdoprFull[fro-1]+" = "+ str(result) +SpdoprFull[to-1]+"\n")
            z = input("Want to check again ? (Y/N)")
            if (z == 'Y') or (z == 'y'):
                SpdRun = True
            else:
                SpdRun = False
        except ValueError :
            print("Invalid Input Please Enter a Integer")
        except IndexError:
            print('\n\tPlease Select an Interger with in The Menu\n')

