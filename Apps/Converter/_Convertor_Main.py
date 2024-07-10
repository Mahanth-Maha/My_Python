import LengthConvertor as lc
import AreaConvertor as ac
import VolumeConvertor as vc
import SpeedConvertor as sp
Run = True
while Run :
    try :
        k= int(input("---------- > MAIN MENU < ----------\nSelect the Type :\n\t1 → Length Conversion\n\t2 → Areal Conversion\n\t3 → Volume Conversion\n\t4 → Speed Conversion\n\n\t0 → Exit\n\nEnterNumber : "))
        if k == 1 :
            lc.RunLengthConvertor()
        elif k == 2 :
            ac.RunAreaConvertor()
        elif k == 3 :
            vc.RunVolConvertor()
        elif k == 4:
            sp.RunSpdConvertor()
        elif k == 0:
            Run = False
        else:
            print("Enter a Valid Option from Menu")
            continue
        z = input("EXIT \n\tAre you Sure ? ( Y :Exit / N :Main Menu ) : ")
        if (z == 'Y') or (z == 'y'):
            Run = False
        else:
            Run = True
    except ValueError:
        print("Enter a Valid Option from Menu")
