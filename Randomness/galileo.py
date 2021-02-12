import math
import statistics 
import random



def roll_d(d): 
    sum_ = 0
    for i in range(d):  
        sum_ += random.randint(1, 6)
    return sum_

def likely_error(t):
    return (1/math.sqrt(t))


def probability_bound(d):
    return (1/pow(6, d))

def dice_simulation (d, a, b):
    num_a, num_b, N = 0, 0, 0
    min_p_bound = probability_bound(d)
    while True:
        N += 1 
        result = roll_d(d)
        # Skip until a or b is generated through iterating a sequence of d die
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
                    
if __name__ == "__main__":
    print("Enter data in format: d a b")
    values = list(map(int, input().strip().split()))
    d, a, b = values
    dice_simulation(d, a, b)
    
    
    
    
    