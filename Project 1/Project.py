import random 

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True
    
print("Comp Turn : Snake(s),water(w) or Gun(g)!")
rand_No = random.randint(1,3)
if rand_No == 1:
    comp ='s'
elif rand_No ==2:
    comp ='w'
elif rand_No ==3:
    comp ='g'
    
you = input("Player's Turn : Snake(s) water(w) or Gun(g)! ")
a = gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is tie")
elif a:
    print("You win!")
else:
    print("You Lose!")
      