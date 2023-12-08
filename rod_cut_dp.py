import math

def cutrod_aux(pricelist, n, memos, sol, cost):
    #if n in memos:
    if memos[n] != -1:
        return memos[n]
    if n == 0:
        memos[n] = 0
        return 0
    bestprice = -math.inf
    for i in range(0, n):
        thisprice = pricelist[i] + cutrod_aux(pricelist, n - (i + 1), memos, sol, cost) - cost
        if thisprice > bestprice:
            sol[n] = i + 1
            bestprice = thisprice
    memos[n] = bestprice
    return bestprice


def cutrod_dp(pricelist, n, cost):
    memos = [-1] * (n+1)
    sol = [-1] * (n+1)
    rv = cutrod_aux(pricelist, n, memos, sol, cost)
    while (n > 0):
        n = n - sol[n]
    if rv == pricelist[n-1] - cost:
        return pricelist[n-1]
    
    return rv

b = [1,5,8,9,10,17,17,20]
c = 2

print(cutrod_dp(b, 8, c))