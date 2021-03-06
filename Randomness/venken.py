import math
import scipy.special as sp

N = 100

def b(n, p, k):
    return sp.comb(n, k) * math.pow(p, k) * math.pow((1-p), n-k)

def get_zscore(x, p):
    mean = N*p
    sigma = math.sqrt(N*p*(1-p))
    return (x-mean)/sigma
    
def p_greater(xlower):
    alpha = 0.0
    for i in range(xlower, N):
        alpha += b(N, p, i)
    return alpha

if __name__ == "__main__":
    i = 0
    alpha, beta = 0, 0
    for i in range(N):
        alpha = 0.0
        for j in range(i, N):
            alpha += b(N, 0.5, j)
        if alpha < 0.05:
            print(f"m: {i} for alpha")
            break
    i = N
    for i in range(N, 0, -1):
        alpha = 0.0
        for j in range(i, N):
            alpha += b(N, 0.7, j)
        if 1-alpha < 0.05:
            print(f"beta: {1-alpha}, i: {i}")
            break
            

        
        
        
        
        
    
    
    
    

        