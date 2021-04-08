def quickselect(l, k) :
    length = len(l)
    # Pick a random pivot element from the list, each
    # equally likely
    # pivot = [...]
    l_small = []
    l_big = []
    
    # Put all elements smaller than pivot into l_small, and all
    # # larger elements into l_big.
    # [...]
    
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