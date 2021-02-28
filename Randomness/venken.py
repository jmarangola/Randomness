import math
import scipy.special as sp

N = 100
p = 0.5


def b(n, p, k):
    return sp.comb(n, k) * math.pow(p, k) * math.pow((1-p), n-k)

def get_zscore(x):
    mean = N*p
    sigma = math.sqrt(N*p*(1-p))
    return (x-mean)/sigma
    
def p_greater(xlower):
    alpha = 0.0
    for i in range(xlower, N):
        alpha += b(N, p, i)
    return alpha

if __name__ == "__main__":
    print(p_greater(61))
        
    
    
    
    

        