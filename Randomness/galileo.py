import math
import statistics 
import random



def roll_d(d): 
    sum_ = 0
    for i in range(d):  
        sum_ += random.randint(1, 6)
    return sum

def min_trials(d):
    return pow(6, 2*d)

def dice_simulation (values):
    d, a, b = values
    N = min_trials(d)
    print(f"N: {N}")
    an, bn, a_per, b_per = 0, 0, 0, 0
    for i in range(N):
        #print(i)
        value = roll_d(d)
        if value == a: an += 1
        elif value == b: bn += 1
    a_per = an/N
    b_per = bn/N
    if abs(a_per - b_per) < (1/(pow(6, d))): print("Equal")
    else: print(f"a ({a})") if a_per > b_per else f"b ({b})"
        
if __name__ == "__main__":
    print("Enter data in format: d, a, b")
    values = list(map(int, input().strip().split()))
    dice_simulation(values)
    
    
    