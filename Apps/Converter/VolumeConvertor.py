# Vol => mm2 , cm2, dc2 , m2 ,km2 , Acre2 , Hect2 || Foot(ft2) , Mile (Mi2) , Yard (yd2), Inch (in2)

Volopr = ['ml','cl','dl','l','hl','ft³','yd³','in³','gal']
VoloprFull = [' Millilitre(ml) ',' Centilitre(cl) ',' Decilitre(dl)',' Litre(l) ',' Hectolitre(hl) ',' Cubic foot(ft³) ',' Cubic Yard(yd³) ',' Cubic Inch(in³) ',' Gallon(gal) ']
def con2l(x,v):
    #ml =1,cl =2 ,dl =3 , l=4, hl=5, ft3 = 6,yd3 = 7 ,in3 =8 , gal= 9 
    if v == 1 :
        return x*0.001
    if v == 2 :
        return x*0.01
    if v == 3 :
        return x*0.1
    if v == 4 :
        return x*1.0
    if v == 5 :
        return x*100.0
    if v == 6 :
        return x*28.31680002
    if v == 7 :
        return x*764.5535832
    if v == 8 :
        return x*0.01638703
    if v == 9 :
        return x*3.785117834

def con2ml(m):
    return m*1000.0
def con2cl(m):
    return m*100.0
def con2dl(m):
    return m*10.0
def con2hl(m):
    return m*0.01
def con2ft3(m):
    return m*0.035314
def con2yd3(m):
    return m*0.0013079
def con2in3(m):
    return m*61.023844
def con2gal(m):
    return m*0.26417205


def RunVolConvertor():
    VolRun = True
    while VolRun :
        print("\nVolumetric Operations Menu :\n")
        for i in range(len(VoloprFull)):
            if i%2 == 0 :
                print("\t",i+1,".",VoloprFull[i],end = "\t\t")
            else:
                print("\t",i+1,".",VoloprFull[i])
        print("\n")
        #print("Values : \n\t1.ml\t\t2.cl\t\n\t3.dl\t\t4.l\t\n\t5.hl\t\t6.cubic ft\t\n\t7.cubic ydt\t8.cubic in\t\n\t9.gallon\n")
        try:
            fro = int(input("Convert From : "))
            to = int(input("Convert To : "))
            Val = float(input("Value to Convert "+Volopr[fro-1]+' to '+Volopr[to-1]+' : '))
            m = con2l(Val,fro)
            #ml =1,cl =2 ,dl =3 , l=4, hl=5, ft3 = 6,yd3 = 7 ,in3 =8 , gal= 9 
            if to == 1 :
                result = con2ml(m)
            elif to == 2 :
                result = con2cl(m)
            elif to == 3 :
                result = con2dl(m)
            elif to == 4 :
                result = m
            elif to == 5 :
                result = con2hl(m)
            elif to == 6 :
                result = con2ft3(m)
            elif to == 7 :
                result = con2yd3(m)
            elif to == 8 :
                result = con2in3(m)
            elif to == 9 :
                result = con2gal(m)
            else :
                print("\n Inavlid Operation Request \n\tPlease Select an Option From Menu")
                break
            print("Convertion of "+str(Val)+" from "+Volopr[fro-1]+' to '+Volopr[to-1]+' : '+str(result))
            print("\n\t"+str(Val)+VoloprFull[fro-1]+" = "+ str(result) +VoloprFull[to-1]+"\n")
            z = input("Want to check again ? (Y/N)")
            if (z == 'Y') or (z == 'y'):
                VolRun = True
            else:
                VolRun = False
        except ValueError :
            print("Invalid Input Please Enter a Integer")
        except IndexError:
            print('\n\tPlease Select an Interger with in The Menu\n')
