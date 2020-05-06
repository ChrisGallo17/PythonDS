def backstringCompare(S, T):
    # return true or false
    newS, newT = [], []
    for i in S:
        if i == '#':
            if newS != []:
                newS.pop()
        else:
            newS.append(i)
    for i in T:
        if i == '#':
            if newT != []:
                newT.pop()
        else:
            newT.append(i)
    if newS == newT:
        return True
    else:
        return False