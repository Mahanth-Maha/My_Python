from tkinter import *
from random import randint 


global Score
Score = 0
global evaluated
evaluated=True
#No of Chances to Player Defined here
global WrongAnswersCount
WrongAnswersCount = 5


#Question Here at Row 1 Column 0 span = 7
global question
#que 1 ki , 3 ki 2 ichedam ; que 2,4 ki 1 ichedam ! ante 0,2 ki clr2 inka 1,3 ki clr1 anamata compare cheyalsindhi
question = [" What is the colour of the Text ?"," What colour shown in Text ?"," What is Colour Text's Colour ?","What is the Background Colour ?"]
global randomque
randomque = randint(0,3)

global colours
colours = ["white", "black", "red","orange", "yellow", "green", "blue","aqua","gray","brown"]
randomcolour1 = randint(0,9)
randomcolour2 = randint(0,9)

# FirstQue - tallluka vallu
global QueShow
global ColourShow

#Count ante Timer Royyyy
global count
count = 0

#MainGUI loop startz
root = Tk()
root.title("COLOUR GUESSING GAME")
root.geometry('530x400')
#root.iconbitmap(root,"Numberguess.ico")

def ScoreUpdater():
    global Score
    Score = Score + 1
    ScoreLabel.config(text='Score : '+ str(Score))
    
def WrongAnswersCountUpdater():
    global WrongAnswersCount
    WrongAnswersCount = WrongAnswersCount - 1
    ChanceLabel.config(text='Chances : '+ str(WrongAnswersCount))

def set_count():
    global count
    count = count + 10
    if count == 10:
        countdown()

def GameOver():
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    global b10
    global Score
    global WrongAnswersCount
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    b10.config(state=DISABLED)
    if (WrongAnswersCount == 0):
        countshow.config(text="Game Over - Chances Over",font=("jokerman",22),fg="red")
    else:
        countshow.config(text="Game Over - Time Up",font=("jokerman",22),fg="red")
    Starttab.config(text="Your Score = "+str(Score),fg='#00000f',font=("Fixedsys",10))
    
def countdown():
    global count
    if ( count != 0 and count != -1 ):
        countshow.config(text="Time Remaining : " + str(count) + " seconds")
        count -= 1
        countshow.after(1000,countdown)
    elif (count == 0):
        GameOver()

def Tally():
    global evaluated
    global Score
    global count
    global WrongAnswersCount
    if(evaluated == True):
        if Score <= 44 :
            changeval()
            set_count()
            ScoreUpdater()
        else:
            countshow.config(text="YOU WON",font=("jokerman",22),fg="blue")
            count = -1
    elif(evaluated == False and Score != 0):
        WrongAnswersCountUpdater()
        if(WrongAnswersCount == 0):
            count = 0

def changeval():
    global randomque
    global randomcolour1
    global randomcolour2
    global QueShow
    global ColourShow
    randomque = randint(0, 3)
    randomcolour1 = randint(0, 9)
    randomcolour2 = randint(0, 9)
    if (randomcolour1 == randomcolour2):
        changeval()
    else:
        QueShow.config(text=question[randomque])
        ColourShow.config(text=colours[randomcolour1],fg=colours[randomcolour2],bg=colours[randomcolour1])
    Starttab.config(text="")
    
def evaluate(answered):
    global randomque
    global evaluated
    global randomcolour1
    global randomcolour2
    if (randomque == 1 or randomque == 3):
        if ( answered == randomcolour1 ) :
            evaluated = True
        else:
            evaluated = False
    elif (randomque == 0 or randomque == 2):
        if ( answered == randomcolour2 ) :
            evaluated = True
        else:
            evaluated = False
    Tally()

# FirstQue - tallluka vallu
QueShow = Label(root,text= question[randomque],font=("High Tower Text",16))
QueShow.grid(row=1,column=0,columnspan=7)
ColourShow = Label(root,text= colours[randomcolour1],fg=colours[randomcolour2],bg=colours[randomcolour1],font=("Rockwell",24),padx=70,pady=30)
ColourShow.grid(row=2,column=0,columnspan=7,pady=10)


global countshow
countshow = Label(root,text="Time Remaining : N/A ",fg='#00000f',font=("Fixedsys",14))
countshow.grid(row=7,column=0,columnspan=7,padx=10,pady=10)
global Starttab
Starttab = Label(root,text="Click Correct answer to Start !",fg='#000fff',font=("Fixedsys",14))
Starttab.grid(row=8,column=0,columnspan=7,padx=10)

global ScoreLabel
ScoreLabel = Label(root,text='Score : '+ str(Score),font=("impact",14),fg="blue")
ScoreLabel.grid(row=0,column=5,pady=10,padx=2)
global ChanceLabel
ChanceLabel = Label(root,text='Chances : '+ str(WrongAnswersCount),font=("impact",14),fg="#000fff")
ChanceLabel.grid(row=0,column=0,columnspan = 3,pady=10,padx=2)

Space = Label(root,text="",padx=10)
Space.grid(row=0,column=0)

#Buttons
global b1
global b2
global b3
global b4
global b5
global b6
global b7
global b8
global b9
global b10

b1 = Button(root,text=colours[0],command=lambda : evaluate(0),padx=17,pady=5,font=("Franklin Gothic",14),borderwidth="3")
b2 = Button(root,text=colours[1],command=lambda : evaluate(1),padx=15,pady=5,font=("Franklin Gothic",14),borderwidth="3")
b3 = Button(root,text=colours[2],command=lambda : evaluate(2),padx=25,pady=5,font=("Franklin Gothic",14),borderwidth="3")
b4 = Button(root,text=colours[3],command=lambda : evaluate(3),padx=15,pady=5,font=("Franklin Gothic",14),borderwidth="3")
b5 = Button(root,text=colours[4],command=lambda : evaluate(4),padx=15,pady=5,font=("Franklin Gothic",14),borderwidth="3")

b6 = Button(root,text=colours[5],command=lambda : evaluate(5),padx=15,pady=5,font=("Franklin Gothic",14),borderwidth="3")
b7 = Button(root,text=colours[6],command=lambda : evaluate(6),padx=19,pady=5,font=("Franklin Gothic",14),borderwidth="3")
b8 = Button(root,text=colours[7],command=lambda : evaluate(7),padx=19,pady=5,font=("Franklin Gothic",14),borderwidth="3")
b9 = Button(root,text=colours[8],command=lambda : evaluate(8),padx=26,pady=5,font=("Franklin Gothic",14),borderwidth="3")
b10 = Button(root,text=colours[9],command=lambda : evaluate(9),padx=15,pady=5,font=("Franklin Gothic",14),borderwidth="3")

b1.grid(row=5,column=1,pady=2)
b2.grid(row=5,column=2,pady=2)
b3.grid(row=5,column=3,pady=2)
b4.grid(row=5,column=4,pady=2)
b5.grid(row=5,column=5,pady=2)

b6.grid(row=6,column=1,pady=2)
b7.grid(row=6,column=2,pady=2)
b8.grid(row=6,column=3,pady=2)
b9.grid(row=6,column=4,pady=2)
b10.grid(row=6,column=5,pady=2)

#Check = Button(root,text="Check",command=Tally)
#Check.grid(row=5,column =0)

mainloop()
