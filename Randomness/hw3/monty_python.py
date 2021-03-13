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
        if len(potential_reveals) > 1: switch_to = list(potential_reveals.difference(set((revealed,))))[0]
        else: switch_to = winning_cat
        switch = random.randint(0, 1)
        if switch:
            nswitch += 1
            switch_correct += (winning_cat == switch_to)
        else:
            stay_correct += (winning_cat == user_initial_choice)
    print(f"Total trials: {n}")
    print(f"Number of times user switched: {nswitch}, Number of times user stayed: {n-nswitch}")
    print(f"Proportion of correct switches: {switch_correct/nswitch}\nProportion of correct stays: {stay_correct/(n-nswitch)}")
            
if __name__ == "__main__":
    simulate(10000)
    
            