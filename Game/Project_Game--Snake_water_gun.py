import random
from re import A

def gameWin(comp, you):
# If two values are equal, declare a tie!!    
    if comp == you:
        return None
# Check for all possibilities when comp. chose 's'        
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True  
# Check for all possibilities when comp. chose 'w'        
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True   
# Check for all possibilities when comp. chose 'g'        
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True                    

print("comp turn: Snake(s) Water(w) or Gun(g)?")
randno = random.randint(1,3)
print(randno)
if randno == 1:
    comp = "s"
elif randno == 2:
    comp = "w"   
elif randno == 3:
    comp = "g"
    
you = input("Your Turn: Snake(s) Water(w) or Gun(g)?\n")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"Computer chose {you}")

if a == None:
    print("The game is tie!")
elif a:
    print("you Win!")
else:
    print("you Lose!")