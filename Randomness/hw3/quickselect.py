"""
    Author: John Marangola - marangol@bc.edu
    4/9/2021
    Professor McTague
    Randomness and Computation
    Programming Assignment 2
"""
import random

# Single Randomized Pivot Quickselection:
def quickselect(l, k):
    global counter
    counter += 1
    length = len(l)
    pivot = random.choice(l)
    l_small = []
    l_big = []
    for element in l:
        if element < pivot:
            l_small.append(element)
        elif element > pivot:
            l_big.append(element)
    assert(length == len(l_small) + len(l_big) + 1)
    if k <= len(l_big):
    # kth largest must be in l_big
        res = quickselect(l_big, k)
        return res
    elif k > len(l_big) + 1:
        # kth largest must be in l_small
        res = quickselect(l_small, k - len(l_big) - 1)
        return res
    else:
        return pivot
    
# Double randomized pivot Quickselect variation
def double_variant(l, k):
    global counter
    counter += 1
    if len(l) == 1 and k ==1:
        return l[0]
    length = len(l)
    min_pivot, max_pivot = sorted(random.sample(l, 2))
    smaller, mid, larger  = [], [], []
    for element in l:
        if element < min_pivot:
            smaller.append(element)
        elif min_pivot < element < max_pivot:
            mid.append(element)
        elif element > max_pivot:
            larger.append(element)
    # Perform quickselect variation with two pivots
    len_smaller, len_mid, len_larger = len(smaller), len(mid), len(larger)
    if len_larger == k - 1:
        return max_pivot
    elif len_larger + len_mid == k - 2:
        return min_pivot
    elif k <= len_larger:
        # If the kth value is in the 'larger' subarray
        return double_variant(larger, k)
    elif k > len_larger + len_mid + 2:
        # If the kth value is in the 'smaller' subarray
        return double_variant(smaller, k - (len_larger + len_mid + 2))
    else:
        # If the kth value is in the 'mid' subarray
        return double_variant(mid, k - (len_larger + 1))

if __name__ == "__main__":
    # Simulation Parameters -----
    n_elements = 125
    k = 50
    n_simulations = 20000
    n_pivots = 2
    randomizedElements = True
    # ----------------------------
    
    # Ability to select non-randomized list elements
    if not randomizedElements:
        l = list(range(1, n_elements+1))
    else:  # Create randomized list of n_elements values
        l = []
        potential_choices = list(range(n_elements))
        for i in range(n_elements):
            choice = random.choice(potential_choices)
            potential_choices.remove(choice)
            l.append(choice)
    sum_ = 0 
    # Run Monte-Carlo Simulation
    print("Beginning Monte Carlo Simulation...")
    if n_pivots == 1:
        for i in range(n_simulations):
            counter = 0
            quickselect(l, k)
            sum_ += counter
        print(sum_/n_simulations)
    elif n_pivots == 2:
        for i in range(n_simulations):
            counter = 0
            double_variant(l, k)
            sum_ += counter
        print(sum_/n_simulations)
    else:
        print("Error, invalid number of pivots selected")