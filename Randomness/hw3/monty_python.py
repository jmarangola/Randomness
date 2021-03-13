import random
import math


def run_simulation(n):
    switch_tally, stay_tally = {"total":0, "correct":0}, {"total":0, "correct":0}
    for i in range(n):
        winning_cat = random.randint(1, 3)
        user_initial_choice = random.randint(1, 3)
        potential_reveals = []
        for i in range(1, 4):
            if  i == user_initial_choice or i == winning_cat:
                continue
            potential_reveals.append(i)
        revealed = random.choice(potential_reveals)
        switch = random.range(0, 1)
        if switch:
            switch_tally["total"] += 1
            
        else:
            stay_tally["total"] += 1
    
if __name__ == "__main__":
    run_simulation(1000)
    
            