"""     John Marangola - marangol@bc.edu    
        Randomness and Computation 
        Professor McTague
        4/28/2021
        Riffle Shuffle
"""

import random

# Gilbert-Shannon-Reeds model to simulate human riffle shuffling
def gsr(l):
    cards = l.copy()

# Top-to-Random shuffle, a simplistic shuffling method placing top card in a random position
def top_to_random(l):
    cards = l.copy()
    top = cards.pop(0)
    cards.insert(random.randint(0, len(cards)), top)
    return cards

if __name__ == "__main__":
    x = list(range(10))
