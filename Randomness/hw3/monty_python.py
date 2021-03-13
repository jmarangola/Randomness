import random
import math

            
def simulate(n):
    switch_correct, stay_correct, nswitch = 0, 0, 0
    for j in range(n):
        winning_cat = random.randint(1, 3)
        user_initial_choice = random.randint(1, 3)
        potential_reveals = set()
        for i in range(1, 4):
            if i == user_initial_choice or i == winning_cat:
                continue
            potential_reveals.add(i)
        revealed = random.choice(list(potential_reveals))
        #print(f"User choice: {user_initial_choice}, winning cat: {winning_cat}")
        #print(f"Potential reveals: {potential_reveals}")
        #print(f"revealed: {revealed}")
            
if __name__ == "__main__":
    simulate(10)
    
            