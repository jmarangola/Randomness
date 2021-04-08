import random

counter = 0
def quickselect(l, k):
    global counter
    counter += 1
    length = len(l)
    # Pick a random pivot element from the list, each
    # equally likely
    pivot = random.choice(l)
    print(f"pivot: {pivot}")
    l_small = []
    l_big = []
    # Put all elements smaller than pivot into l_small, and all
    # larger elements into l_big.
    for element in l:
        if element < pivot:
            l_small.append(element)
        elif element > pivot:
            l_big.append(element)
    # We assume all elements are distinct, so (besides the pivot) every element# should go into l_small or l_big
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
    
# Two pivot quickselect variant
def double_variant(l, k):
    global counter
    counter += 1
    length = len(l)
    min_pivot, max_pivot = sorted(random.sample(l, 2))
    first, mid, last  = [], [], []
    for element in l:
        if element < min_pivot:
            first.append(element)
        elif min_pivot < element < max_pivot:
            mid.append(element)
        elif element > max_pivot:
            last.append(element)
            
    # perform quickselect variation with two pivots


if __name__ == "__main__":
    arr = list(range(10))
    print(quickselect(arr, 2))
    print(f"n calls: {counter}")   
