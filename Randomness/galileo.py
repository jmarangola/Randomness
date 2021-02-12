"""
    Author: John Marangola
    Randomness and Computation
    Programming Assignment 1 - Galileo
    2/12/2021
    Professor McTague
"""

import math
import statistics 
import random

def roll_d(d): # Returns the simulated, pseudo-random sum of d fair die rolled together
    sum_ = 0
    for i in range(d):  sum_ += random.randint(1, 6)
    return sum_

def likely_error(t): return (1/math.sqrt(t)) # Compute likely error bound for t trials

def probability_bound(d): return (1/pow(6, d)) 

def dice_simulation (d, a, b):
    """Computes approximate relative probabilities for d rolls of a fair six sided die to sum to a, b

    Args:
        d (int): [number of dice]
        a (int): [value a]
        b (int): [value b]
    """
    num_a, num_b, N = 0, 0, 0
    min_p_bound = probability_bound(d)
    while True:
        N += 1 
        result = roll_d(d)
        if result != a and result != b: 
            continue
        if result == a:
            num_a += 1
        else:
            num_b += 1
        a_prop, b_prop = num_a/N, num_b/N
        if abs(a_prop - b_prop) + 2*likely_error(N) < min_p_bound:
            print("Equal")
            break
        if abs(a_prop - b_prop) - 2*likely_error(N) > 0:
            if a_prop > b_prop:
                print(f"{a} is more likely.") 
            else:
                print(f"{b} is more likely")
            break

def run_simulation(termination_strings=["D", "DONE"]):
    """Continually accept input and run simulation until a termination string is recieved 

    Args:
        termination_strings (list, optional): [List of valid termination string(s)]. Defaults to ["D", "DONE"].
    """
    while True:
        try:
            print("Enter data in format: d a b")
            raw_data = input()
            values = list(map(int, raw_data.strip().split()))
            d, a, b = values
            dice_simulation(d, a, b)
        except:
            if raw_data.upper() in termination_strings: break
            run_simulation() 
                     
if __name__ == "__main__":
    run_simulation()
        
    
    
    
    