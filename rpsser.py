#%%
#It could be carried by an African swallow!

#import modules of course, pillow for images maybe
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
import functools
from functools import partial
import PIL
from PIL import ImageTk, Image

#define the window to be made first. He doesn't fight for the users
main = tk.Tk()
main.title("Master Control Program")


#then define the frames to be used
framer1 = tk.Frame(relief=tk.SUNKEN,borderwidth=10)
framer2 = tk.Frame()
framer3 = tk.Frame()
framer4 = tk.Frame()
framer5 = tk.Frame()
framer6 = tk.Frame()
framer7 = tk.Frame()
framer8 = tk.Frame()
framer9 = tk.Frame()


#Next, define some of the widgets and labels
title = tk.Label(
    text="Rock, Paper, Scissors!",
    fg="#C10298",
    font=("Comic Sans MS", 50),
    master=framer1
)
title.pack()


diff = tk.Label(
    text="Choose your difficulty!",
    font=("", 30),
    master=framer2
)
diff.pack()

#define dictionaries and global variables to be used later
throwdict = {1:"Rock", 2:"Paper", 3:"Scissors"}
throwintdict = {"Rock":1, "Paper":2, "Scissors":3, "":4}
mod3dict = {0:"Rock", 1:"Paper", 2:"Scissors"}
mod3intdict = {"Rock":0, "Paper":1, "Scissors":2, "":4}
hiddendiff = tk.StringVar()
hiddenpastprog = tk.StringVar()
hiddenpastres = tk.StringVar()

#define the command to differentiate which difficulty button is
#pressed, and set the global variable value to that setting
#allows multiple runs of one difficulty to be run AND also allows
#changing of the difficulty in the same open instance
def pressdiff(button):

    if button == "easy":
        hiddendiff.set(value="Easy")
    elif button == "normal":
        hiddendiff.set(value="Normal")
    elif button == "hard":
        hiddendiff.set(value="Hard")
    elif button == "impossible":
        hiddendiff.set(value="Impossible")

    #also erase throws to set it fresh for each choice
    usert.config(text="")
    programt.config(text="")
    resultst.config(text="")
    hiddenpastprog.set(value="")
    hiddenpastres.set(value="")


#actually show the buttons for difficulties
easy = tk.Button(
    text="Easy",
    font=("", 20),
    width=8,
    height=4,
    fg="#05B339",
    command=partial(pressdiff, button="easy"),
    #hardcoded with strings vs variable names because the names
    #are not being recognized
    master=framer3
)
easy.pack(side="left")
#orient the buttons to the left so they all fit in the same frame
#and i don't need to use x,y coordinates to get them nicely spaced

normal = tk.Button(
    text="Normal",
    font=("", 20),
    width=8,
    height=4,
    fg="#ACB806",
    command=partial(pressdiff, button="normal"),
    master=framer3
)
normal.pack(side="left")

hard = tk.Button(
    text="Hard",
    font=("", 20),
    width=8,
    height=4,
    fg="#E67A0E",
    command=partial(pressdiff, button="hard"),
    master=framer3
)
hard.pack(side="left")

impossible = tk.Button(
    text="Impossible",
    font=("", 20),
    width=8,
    height=4,
    fg="#FF1900",
    command=partial(pressdiff, button="impossible"),
    master=framer3
)
impossible.pack(side="left")



#title text for throw
throw = tk.Label(
    text="Choose your throw!",
    font=("", 30),
    master=framer4
)
throw.pack()



#define labels to differentiate user and program throws and results
#so I can modify them with the throw choices
usert = tk.Label(
    text="",
    #userthrowtext isn't defined here but throw is??
    #oh cause it's within the press, so outside of it 
    #the program has no idea
    font=("", 20),
    width=12,
    height=4,
    master=framer8,
    )
usert.pack(side="left")

programt = tk.Label(
    text="",
    font=("", 20),
    width=12,
    height=4,
    master=framer8,
)
programt.pack(side="left")

resultst = tk.Label(
    text="",
    font=("", 30),
    width=16,
    height=2,
    master=framer9
)
resultst.pack()

#differentiate which throw the user picks
def pressthrow(throw):
    usert.config(text=throw)
    #define the user's throw label to be the... user's throw...

    #now for the program's response
    if hiddendiff.get() == "Easy":
        #easy always loses, so I can hardcode results and choices
        #doesn't work if you choose the throw first and THEN the
        #difficulty, but can fix later

        if throw == "Rock":
            programt.config(text="Scissors")
        elif throw == "Paper":
            programt.config(text="Rock")
        elif throw == "Scissors":
            programt.config(text="Paper")            
        resultst.config(text="User wins!")

    if hiddendiff.get() == "Normal":
        #normal is just a random throw, done by a random number
        ran = np.random.randint(1,4)
        throwint = throwintdict[throw]
        ranstr = throwdict[ran]
        programt.config(text=ranstr)
        #bit clunky dictionary work but fine for now

        if ran == throwint:
            resultst.config(text="Tie!")
        elif ran == 1 and throwint == 3:
            resultst.config(text="Program wins!")
            #had to hardcode this, as since 3>1 it counted this
            #as user wins instead. Might overhaul this later
        elif ran < throwint or (ran == 3 and throwint == 1):
            resultst.config(text="User wins!")
        else:
            resultst.config(text="Program wins!")
        del ran

    if hiddendiff.get() == "Hard":
        #so the big secret about this is based on a mark rober vid lol
        #but that humans typically follow a specific pattern in rock, paper, scissors
        #and you can counteract that. now the trouble is this involves
        #"remembering" previous games, so im gonna need to store past games
        #in variables, but thankfully it's just t-1 so not that big a deal
        #but hoping i can pull this off and learn a bit

        #so when it's the first game, throw rock and record the program threw
        #rock and whether it won or not. on the second, remember your throw
        #and if you won, go up. if tie or lost, go down. then throw that,
        #record THAT throw as the new t-1 throw, and also whether you won.
        #then it just keeps going

        pastint = mod3intdict[hiddenpastprog.get()]
        throwint = throwintdict[throw]
        #turn the throws into integers to move along the chain easily
        #for the rest of the comparison I used 1,2,3 but I decided to use
        #mod 3 counting for this which uses 0,1,2. Instead of just putting
        #everything into 0,1,2 I just made separate dictionaries for the mod 3
        #logic and then switched back to strings as the common

        if hiddenpastprog.get() == "":
            #if this is the first game as the past throw string is empty...
            programt.config(text="Rock")
            hiddenpastprog.set(value="Rock")

            if throwint == 1:
                resultst.config(text="Tie!")
                hiddenpastres.set(value="tie")
            elif throwint == 2:
                resultst.config(text="User wins!")
                hiddenpastres.set(value="lost")
            elif throwint == 3:
                resultst.config(text="Program wins!")
                hiddenpastres.set(value="won")
            #hardcoded since the program always leads with rock

        elif hiddenpastprog.get() != "":
            #if this is the second or more game with the past throw string filled...
            if hiddenpastres.get() == "won":
                newprogint = (pastint+1)%3
                newgoodprogint = newprogint + 1
                newprog = mod3dict[newprogint]
                programt.config(text=newprog)
                #turn string throws into mod 3 integers, move along the chain,
                #convert back into strings AND the 1,2,3 integers to compare

                if newgoodprogint == throwint:
                    resultst.config(text="Tie!")
                    hiddenpastprog.set(value=newprog)
                    hiddenpastres.set(value="tie")
                elif newgoodprogint == 1 and throwint == 3:
                    resultst.config(text="Program wins!")
                    hiddenpastprog.set(value=newprog)
                    hiddenpastres.set(value="won")
                elif newgoodprogint < throwint or (newgoodprogint == 3 and throwint == 1):
                    resultst.config(text="User wins!")
                    hiddenpastprog.set(value=newprog)
                    hiddenpastres.set(value="lost")
                else:
                    resultst.config(text="Program wins!")
                    hiddenpastprog.set(value=newprog)
                    hiddenpastres.set(value="won")
                #if the program won last time, move down the chain (rock to paper)
                #and now compare just like for normal, but record whether
                #the program won or lost and what they threw in string form
                

            else:
                newprogint = (pastint-1)%3
                #also counting ties as "losses" but not sure if
                #the research backs that up....anyway–
                newgoodprogint = newprogint + 1
                newprog = mod3dict[newprogint]
                programt.config(text=newprog)

                if newgoodprogint == throwint:
                    resultst.config(text="Tie!")
                    hiddenpastprog.set(value=newprog)
                    hiddenpastres.set(value="tie")
                elif newgoodprogint == 1 and throwint == 3:
                    resultst.config(text="Program wins!")
                    hiddenpastprog.set(value=newprog)
                    hiddenpastres.set(value="won")
                elif newgoodprogint < throwint or (newgoodprogint == 3 and throwint == 1):
                    resultst.config(text="User wins!")
                    hiddenpastprog.set(value=newprog)
                    hiddenpastres.set(value="lost")
                else:
                    resultst.config(text="Program wins!")
                    hiddenpastprog.set(value=newprog)
                    hiddenpastres.set(value="won")
            
            #if the program lost OR tied last game, move up the chain (paper to rock)
            #and compare and record the results and the throw...
            #huh i could probably just move the throw recording outside since it's in everything...
        
    if hiddendiff.get() == "Impossible":
        if throw == "Rock":
            programt.config(text="Paper")
        elif throw == "Paper":
            programt.config(text="Scissors")
        elif throw == "Scissors":
            programt.config(text="Rock")            
        resultst.config(text="Program wins!")

        #hardcoded because impossible is not meant to be winnable >:)

    

    
#outside of what happens when a throw is pressed, make the buttons to
#select a throw in the first place, packing them in the same frame as before
rock = tk.Button(
    text="Rock",
    font=("", 20),
    width=8,
    height=4,
    fg="#343434",
    command=partial(pressthrow, throw="Rock"),
    master=framer5
)
rock.pack(side="left")

paper = tk.Button(
    text="Paper",
    font=("", 20),
    width=8,
    height=4,
    fg="#D1A2A2",
    command=partial(pressthrow, throw="Paper"),
    master=framer5
)
paper.pack(side="left")

scissors = tk.Button(
    text="Scissors",
    font=("", 20),
    width=8,
    height=4,
    fg="#3934C5",
    command=partial(pressthrow, throw="Scissors"),
    master=framer5
)
scissors.pack(side="left")


#next differentiate the throws of the user and program to show to the user

result = tk.Label(
    text="Results!",
    font=("", 30),
    master=framer6
)
result.pack()

userchoice = tk.Label(
    text="User:",
    font=("", 15),
    width=16,
    master=framer7
)
userchoice.pack(side="left")

programchoice = tk.Label(
    text="Program:",
    font=("", 15),
    width=16,
    master=framer7
)
programchoice.pack(side="left")

#then pack all the frames and activate the main loop for the GUI
framer1.pack()
framer2.pack()
framer3.pack()
framer4.pack()
framer5.pack()
framer6.pack()
framer7.pack()
framer8.pack()
framer9.pack()

main.mainloop()
# %%
