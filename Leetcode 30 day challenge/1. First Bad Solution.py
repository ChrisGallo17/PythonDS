def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    l = 0
    r = n
    while l < r:
        mid = l + (r - l) // 2
        if not isBadVersion(mid):
            l = mid + 1
        else:
            r = mid
    
    return l

test = [False, False, False, False, False,
        True, True, True, True, True, True, 
        True, True, True, True]

def isBadVersion(n):
    return test[n - 1]

firstBadVersion(len(test))