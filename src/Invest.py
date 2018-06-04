import numpy as np
import matplotlib.pyplot as plt

def PeriodEvol( previous, deposit, returnRate,  fee, feeWrapper, profitTax ) :
    previousInterest = previous * (1+returnRate)
    fee = previous * (fee+feeWrapper)
    periodProfit = previous*returnRate * profitTax
    return deposit + previousInterest - fee - periodProfit    

def Evolution(
        initDeposit = 0
        , periodDeposit = 0
        , returnRate = 0
        , nPeriod = 30
        , entryFee = 0
        , periodFee = 0
        , exitFee = 0
        , entryFeeWrapper = 0
        , periodFeeWrapper = 0
        , exitFeeWrapper = 0
        , periodProfitTax = 0
        , finalProfitTax = 0
        
) :
    """
    This function returns the value of portfolio as a function of time.
    A simplistic annual model is used.
    """

    evol = [ initDeposit * (1-entryFee)*(1-entryFeeWrapper)]

    while len(evol)<=nPeriod :
        evol.append( PeriodEvol( evol[-1]
                                 , periodDeposit*(1-entryFee)*(1-entryFeeWrapper)
                                 , returnRate
                                 , periodFee
                                 , periodFeeWrapper
                                 , periodProfitTax
                                 ) )

    evol[-1] *= (1-exitFee)*(1-exitFeeWrapper)

    finalProfit = evol[-1]-nPeriod*periodDeposit - initDeposit
    evol[-1] -= finalProfit * finalProfitTax
    
    return evol


