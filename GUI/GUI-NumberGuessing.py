# NUMBER GUESSING GAME IN PY USING TKINTER

#modules
from tkinter import *
from random import randint 

#random number 
global m
m = randint(1, 9) * 100 + randint(0, 9) * 10 + randint(0, 9)
global Trailno
Trailno =0

# GUI
root = Tk()
root.title("NUMBER GUESSING GAME")
root.geometry('320x330')

#Game Title and discription
Title = Label(root,text="Guessing The Number",font=('forte',22),padx=30,pady=10,fg = 'blue')
Title.grid(row=0,column=0)

Discription = Label(root,text="( Guess from 100 to 999 )",font=('forte',12),padx=50,fg='#ff00ff')
Discription.grid(row=1,column=0)

#Main Operator
def AllOper():
    global Trailno
    global inputed
    #Total Trials to player is 15
    if ( Trailno >= 0 and Trailno <15 ) :
        try :
            answered = int(inputed.get())
            if (answered > 99 and answered < 1000) :
                Trailno = Trailno + 1
                Trails.config(text="Trails : " + str(Trailno) + " Out of 15")
                if answered == m :
                    Indicator.config(text="Correct Answer",font=("jokerman",20),fg="Green")
                    victory = Label(root,text = "You Won with " + str(Trailno) + " Trails")
                    victory.grid(row=9,column=0)
                    Check.config(state = DISABLED)
                else:
                    if Trailno >= 3 :
                        if answered > m :
                            Hint.config(text= "Hint : the value is Lesser than " + str(answered),fg='#3e3e3e')
                        elif answered < m :
                            Hint.config(text= "Hint : the value is Greater than " + str(answered),fg='#2d2d2d')
                    Indicator.config(text="No,Not " + str(answered) +" Try Again",fg='red')
            else:
                Indicator.config(text="Enter Correct Value b/w 100 - 999",fg='red')
        except ValueError :
            Indicator.config(text="Enter Correct Value b/w 100 - 999",fg='red')
        inputed.delete(0,END)
    elif(Trailno == 15):
        Indicator.config(text=" - G A M E - O V E R - ",font=("jokerman",20),fg="red")
        Losser = Label(root, text="No luck You exceeded 15 Trails & No is " + str(m))
        Losser.grid(row=9, column=0)
        Check.config(state=DISABLED)


# Trails Shower
global Trails
Trails = Label(root,text="Trails : " + str(Trailno) + " Out of 15",anchor='e')
Trails.grid(row=2,column=0,pady=15)
# Input Tab
global inputed
inputed = Entry(root,borderwidth=5)
inputed.grid(row=3,column =0)
# Check Button
global Check
Check = Button(root,text="Check",command=AllOper,bg = 'aqua')
Check.grid(row=5,column =0,pady=10,padx=20)
# Results Tab
global Indicator
Indicator = Label(root,text = "Start the game")
Indicator.grid(row=7,column=0)
# Hint Tab
global Hint
Hint = Label(root,text= "Hint : Avaliable from Trail 3 ",fg='#4e4e4e')
Hint.grid(row = 8,column=0)

#Main loop for GUI
mainloop()
