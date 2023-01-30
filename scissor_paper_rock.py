#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# SCISSOR-PAPER-ROCK GAME


# In[6]:


import random

def win(computer,you):
    if computer==you:
        return None
    elif(computer=='r'):
        if(you=='s'):
            return False
        elif(you=='p'):
            return True
        
    elif(computer=='p'):
        if(you=='r'):
            return False
        elif(you=='s'):
            return True
        
    elif(computer=='s'):
        if(you=='p'):
            return False
        elif(you=='r'):
            return True


print("Computer turn: Rock(r), Paper(p), Scissor(s) ")
num = random.randint(1,3)
if(num==1):
    computer = 'r'
elif(num==2):
    computer = 'p'
elif(num==3):
    computer = 's'

you = input("Yours turn: Rock(r), Paper(p), Scissor(s)? ")
final=win(computer,you)

print(f"Computer chose {computer}")
print(f"You chose {you}")

if(final==None):
    print("The game is Tie!")
elif final:
    print("You Win!")
else:
    print("You Lose!")


# In[ ]:




