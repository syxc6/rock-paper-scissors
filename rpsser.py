#%%
print("It could be carried by an African swallow!")


import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
from functools import partial


#%%
glass = tk.Tk()
##glass.mainloop()
glass.title("An African swallow mayBE, but not a EuroPEAN swallow, that's my point")

raining = tk.Frame(relief=tk.RIDGE, borderwidth=10)
raining.pack()

hello = tk.Label(
    text="....but then of course, African swallows are nonmigratory",
    foreground="#f0f94a",
    background="#59C672",
    width=70,
    height=10,
    master=raining)
hello.pack()

write = tk.Entry(bg="red", fg="yellow", width=50)
write.pack()

def yoink():
    quote = write.get()
    print(quote)
    ##there are text boxes and other alterations of text one can use
    ##.....anyway!

press = tk.Button(
    text="you wouldn't dare...",
    command=yoink,
    width=25,
    height=25,
    bg="#AF1717",
    ##background colors for buttons apparently infamously dont work on macs....great 
    fg="#920C97"
)
press.pack()

##using button "press" involves going inside the button

write.bind("<Return>", lambda event: yoink())
##write.pack()
##using enter key, does NOT need pack after it, but the button
##needs the yoink defined before it to work. then the button
##OR enter will output



glass.mainloop()

#%%
#define the window to be made first, with a nod to Tron of course
main = tk.Tk()
main.title("Master Control Program")


#first define the frames to be used
framer1 = tk.Frame(relief=tk.SUNKEN,borderwidth=10)
framer2 = tk.Frame()
framer3 = tk.Frame()
framer4 = tk.Frame()
framer5 = tk.Frame()
framer6 = tk.Frame()
framer7 = tk.Frame()
framer8 = tk.Frame()


#Next, to make sense to me, define widgets in order of top to bottom
#as I think they'll show up on the screen. i'll add in the difficulty
#and choices being buttons later... actually that would probably be
#easier than just redoing the text? FUCK IT BUTTONSSSS
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

#define how to read which difficulty is present
def pressdiff(userdiff):
    print(userdiff)
    nothing = 0



#insert buttons for difficulty
easy = tk.Button(
    text="Easy",
    font=("", 20),
    width=8,
    height=4,
    fg="#05B339",
    command=partial(pressdiff),
    master=framer3
)
easy.pack(side="left")

normal = tk.Button(
    text="Normal",
    font=("", 20),
    width=8,
    height=4,
    fg="#ACB806",
    command=partial(pressdiff),
    master=framer3
)
normal.pack(side="left")

hard = tk.Button(
    text="Hard",
    font=("", 20),
    width=8,
    height=4,
    fg="#E67A0E",
    command=partial(pressdiff),
    master=framer3
)
hard.pack(side="left")

impossible = tk.Button(
    text="Impossible",
    font=("", 20),
    width=8,
    height=4,
    fg="#FF1900",
    command=partial(pressdiff),
    master=framer3
)
impossible.pack(side="left")



#text for throw
throw = tk.Label(
    text="Choose your throw!",
    font=("", 30),
    master=framer4
)
throw.pack()


#gonna try to make buttons using left, right instead of entirely new
#frames for all of them...ugh
#command for these will be to define a variable, and then once it's
#used to delete it... except for the possibly adaptive bot... heh heh heh...
rock = tk.Button(
    text="Rock",
    font=("", 20),
    width=8,
    height=4,
    fg="#343434",
    master=framer5
)
rock.pack(side="left")

paper = tk.Button(
    text="Paper",
    font=("", 20),
    width=8,
    height=4,
    fg="#D1A2A2",
    master=framer5
)
paper.pack(side="left")

scissors = tk.Button(
    text="Scissors",
    font=("", 20),
    width=8,
    height=4,
    fg="#3934C5",
    master=framer5
)
scissors.pack(side="left")


#next show the different throws of the user and program and
#add in the program's functionality

result = tk.Label(
    text="Results:",
    font=("", 30),
    master=framer6
)
result.pack()


#now for the actual choices
#userres = tk.Label(
    #text=userthr
    #define userthr to be from the button picked...somehow
#)
#userres.pack(side="left")



diff = np.array([1, 2, 3])
easy = np.array([1, 2, 3])
normal = np.array([1, 2, 3])
hard = np.array([1, 2, 3])


#userdiffstr = input("Difficulty? Easy=1, Normal=2, Impossible=3")
#userdiff = int(userdiffstr)

#userthrowstr = input("Throw? Rock=1, Paper=2, Scissors=3")
#userthrow = int(userthrowstr)

#throwdict = {1:"Rock", 2:"Paper", 3:"Scissors"}

#print("User: " + throwdict[userthrow])

#if userdiff == 1:
    #print("wow you picked a real challenge.")

#elif userdiff == 2:
    #ran = np.random.randint(1,4)
    ##Copied from rps, seems to define ran the first time and then remember
    ##the value each subsequent run. need to clear the memory with del
    #print("Program: " + throwdict[ran])
    #if ran == userthrow:
        #print("Tie!")
    #elif ran < userthrow or ran == 3 and userthrow == 1:
        #print("User wins!")
    #else:
        #print("Program wins!")
    #del ran

#elif userdiff == 3:
    #print("Go back to Dark Souls.")

framer1.pack()
framer2.pack()
framer3.pack()
framer4.pack()
framer5.pack()
framer6.pack()
framer7.pack()
framer8.pack()

main.mainloop()
# %%
