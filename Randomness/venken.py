import math
import scipy.special as sp

def b(n, p, k):
    return sp.binom(n, k) * pow(p, k) * pow(p, n-k)

def test_range():
    pass

if __name__ == "__main__":
    print(b(6, 0.5, 3))