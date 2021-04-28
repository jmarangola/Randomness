"""     John Marangola - marangol@bc.edu    
        Randomness and Computation 
        Professor McTague
        4/28/2021
        Riffle Shuffle
"""

import random

# Gilbert-Shannon-Reeds model to simulate human riffle shuffling
def gsr(l):
    size = len(l)
    cards = l.copy()
    random_seq, left, right, riffle = [], [], [], []
    n_right = 0
    for i in range(size):
        flip = random.randint(0, 1)
        if flip: 
            n_right += 1        
        random_seq.append(flip)
    # Cut the deck into left and right halves:
    left = [cards[i] for i in range(size - n_right)]
    right  = [cards[i] for i in range(size - n_right, size)]
    for x in range(size):
        if random_seq[x]:
            riffle.append(right.pop(0))
        else:
            riffle.append(left.pop(0))
    return riffle
    
    
# Top-to-Random shuffle, a simplistic shuffling method placing top card in a random position
def top_to_random(l):
    cards = l.copy()
    top = cards.pop(0)
    cards.insert(random.randint(0, len(cards)), top)
    return cards

if __name__ == "__main__":
    pass