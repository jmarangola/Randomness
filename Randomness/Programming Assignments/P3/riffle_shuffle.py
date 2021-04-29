"""     John Marangola - marangol@bc.edu    
        Randomness and Computation 
        Professor McTague
        4/28/2021
        Riffle Shuffle Analysis Programming Assignment
"""

import random
import os

def slow_gsr(l):
    """ An intuituve implementation Gilbert-Shannon-Reeds model to simulate human riffle shuffling

    Args:
        l (list): Unshuffled deck of cards

    Returns:
        [list]: Shuffled deck of cards after a single iteration
    """
    size = len(l)
    random_seq, left, right, riffle = [], [], [], []
    n_right = 0
    for i in range(size):
        flip = random.randint(0, 1)
        if flip: 
            n_right += 1        
        random_seq.append(flip)
    # Cut the deck into left and right halves:
    left = [l[i] for i in range(size - n_right)]
    right  = [l[i] for i in range(size - n_right, size)]
    for x in range(size):
        if random_seq[x]:
            riffle.append(right.pop(0))
        else:
            riffle.append(left.pop(0))
    return riffle


def gsr(l):
    """ An more optimized GSR implementation to simulate riffle-shuffling of an len(l) size deck of cards

    Args:
        l (list): Unshuffled deck of cards

    Returns:
        [list]: Shuffled deck of cards after a single GSR iteration
    """
    size = len(l)
    random_seq, riffle = [], []
    n_right = 0
    for i in range(size):
        flip = random.randint(0, 1)
        if flip: 
            n_right += 1        
        random_seq.append(flip)
    start_right = size - n_right 
    start_left = 0
    for x in range(size):
        if random_seq[x]: # from right sub-array
            riffle.append(l[start_right])
            start_right += 1
        else:
            riffle.append(l[start_left])
            start_left += 1        
    return riffle
    

def top_to_random(l):
    """ Top-to-Random shuffle, a simplistic shuffling method placing top card in a random position

    Args:
        l (list): Unshuffled deck of cards

    Returns:
        [list]: Shuffled deck of cards
    """
    cards = l.copy()
    top = cards.pop(0)
    cards.insert(random.randint(0, len(cards)), top)
    return cards

# Returns true if i comes before j in l
def test_order(i, j, l):
    return (l.index(i) < l.index(j))

def monte_carlo_simulation(n, i, j, k, N=10000, simulation_type="gsr", running_output_on=True):
    """ Simulate the outcome of N shuffles using either GSR or Top-to-Random Shuffling

    Args:
        n (int): Size of deck 
        i (int): element i
        j (int): element j
        k (int): Number of shuffles 
        N (int, optional): Number of simulation trials. Defaults to 10000.
        simulation_type (str, optional): 'top' for TRS simulation, 'gsr' to simulate GSR. Defaults to "gsr".
        running_output_on (bool, optional): Display simulation status during runtime. Defaults to True.
    """
    if max(i, j) > n: 
        print("ERROR")
        return
    unshuffled = list(range(n))
    n_ifirst_gsr, n_ifirst_top = 0, 0
    if simulation_type == "top":
        for x in range(N):
            temp = unshuffled.copy()
            for y in range(k):
                temp = top_to_random(temp)
            n_ifirst_top += int(test_order(i, j, temp))
        print(f"Top to Random:\nProb. i ({i}) before j ({j}): {n_ifirst_top/N} | Prob. j ({j}) before i ({i}): {(N - n_ifirst_top)/N}")
    elif simulation_type == "gsr":
        for x in range(N):
            temp = list(range(n))
            for y in range(k):
                temp = gsr(temp)
            n_ifirst_gsr += int(test_order(i, j, temp))
            if running_output_on: print(f"Percent Complete {100*(x+1)/10000}")
        print(f"Riffle-Shuffle:\nProb. of i ({i}) before j ({j}): {n_ifirst_gsr/N} | Prob. j ({j}) before i ({i}): {(N - n_ifirst_gsr)/N}")
       

if __name__ == "__main__":
    monte_carlo_simulation(10, 0, 1, 1, simulation_type="gsr")