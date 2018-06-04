def Cost( fees, frequence=100, maxVal=3000) :
    """
    Return the relative cost from a set of (cost, limit) tuples
    """

    fees = sorted( fees, key = lambda x : x[1] )

    cost=[]
    amounts = range(0, maxVal+1, frequence)
    for val in amounts :
        while val > fees[0][1] : fees= fees[1:]

        fee = fees[0][0]
        if val == 0 : fee = 0
        elif fee > 0.2 : fee /= val

        cost.append(fee)
    
    return cost
        
        
