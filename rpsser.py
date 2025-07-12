#%%
print("It could be carried by an African swallow!")


import numpy as np
import tkinter as tk
import tkinter.ttk as ttk


#%%
glass = tk.Tk()
#glass.mainloop()
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
    #there are text boxes and other alterations of text one can use
    #.....anyway!

press = tk.Button(
    text="you wouldn't dare...",
    command=yoink,
    width=25,
    height=25,
    bg="#AF1717",
    #background colors for buttons apparently infamously dont work on macs....great 
    fg="#920C97"
)
press.pack()

#using button "press" involves going inside the button

write.bind("<Return>", lambda event: yoink())
#write.pack()
#using enter key, does NOT need pack after it, but the button
#needs the yoink defined before it to work. then the button
#OR enter will output



glass.mainloop()

#%%
diff = np.array([1, 2, 3])
easy = np.array([1, 2, 3])
normal = np.array([1, 2, 3])
hard = np.array([1, 2, 3])

userdiffstr = input("Difficulty? Easy=1, Normal=2, Impossible=3")
userdiff = int(userdiffstr)

userthrowstr = input("Throw? Rock=1, Paper=2, Scissors=3")
userthrow = int(userthrowstr)

throwdict = {1:"Rock", 2:"Paper", 3:"Scissors"}

print("User: " + throwdict[userthrow])

if userdiff == 1:
    print("wow you picked a real challenge.")

elif userdiff == 2:
    ran = np.random.randint(1,4)
    #Copied from rps, seems to define ran the first time and then remember
    #the value each subsequent run. need to clear the memory with del
    print("Program: " + throwdict[ran])
    if ran == userthrow:
        print("Tie!")
    elif ran < userthrow or ran == 3 and userthrow == 1:
        print("User wins!")
    else:
        print("Program wins!")
    del ran

elif userdiff == 3:
    print("Go back to Dark Souls.")
# %%
