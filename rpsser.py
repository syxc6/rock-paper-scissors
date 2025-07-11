#%%
print("It could be carried by an African swallow!")

import numpy as np

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
