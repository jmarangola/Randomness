"""
Author: John Marangola 
        Professor McTague
        Randomness and Computation
        Lecture 5 Written Homework
"""
import random
import math

            
def simulate(n):
    """Monte Carlo Simulation for n trials of the Monte Python Problem
    Args:
        n (int): number of trials
    """
    switch_correct, stay_correct, nswitch = 0, 0, 0 # Variables to keep track of the results of simulation
    for j in range(n):
        winning_cat = random.randint(1, 3) # Attacker randomly generates correct cat
        user_initial_choice = random.randint(1, 3) # Users initial guess
        potential_reveals = set()
        for i in range(1, 4):
            if i == user_initial_choice or i == winning_cat: # Cannot reveal correct cat or users initial choice--the attacker likes to play with their food
                continue
            potential_reveals.add(i)
        revealed = random.choice(list(potential_reveals))
        # Determine the user's potential switched guess (if simulation decides user switches below) 
        if len(potential_reveals) > 1:
            switch_to = list(potential_reveals.difference(set((revealed,))))[0]
        else: 
            switch_to = winning_cat
        switch = random.randint(0, 1) # Randomly simulate decision to switch
        if switch:
            nswitch += 1
            switch_correct += (winning_cat == switch_to)
        else:
            stay_correct += (winning_cat == user_initial_choice)
    # Output results
    print(f"Total trials: {n}")
    print(f"Number of times user switched: {nswitch}, Number of times user stayed: {n-nswitch}")
    print(f"Proportion of correct switches: {switch_correct/nswitch}\nProportion of correct stays: {stay_correct/(n-nswitch)}")
            
if __name__ == "__main__":
    # Simulate n times
    n = 100000
    simulate(n)
    
            