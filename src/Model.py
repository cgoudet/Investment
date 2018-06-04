import src.Invest as inv

class InvestBenchmark :
    nPeriod = 30
    initDeposit = 0
    periodDeposit = 0

    def __init__(self, dico={} ) :
        if 'initDeposit' in dico : self.initDeposit = dico['initDeposit']
        if 'periodDeposit' in dico : self.periodDeposit = dico['periodDeposit']
        if 'nPeriod' in dico : self.nPeriod = dico['nPeriod']

#==========
class InvestModel() :

    name = 'InvestModel'
    returnRate = 0
    entryFee=0
    periodFee=0
    exitFee=0
    entryFeeWrapper=0
    periodFeeWrapper=0
    exitFeeWrapper=0
    periodProfitTax=0
    finalProfitTax=0
    
    def __init__( self, dico = {} ) :

        if 'name' in dico : self.name = dico['name']
        if 'returnRate' in dico : self.returnRate = dico['returnRate']
        if 'entryFee' in dico : self.entryFee = dico['entryFee']
        if 'periodFee' in dico : self.periodFee = dico['periodFee']
        if 'exitFee' in dico : self.exitFee = dico['exitFee']
        if 'entryFeeWrapper' in dico : self.entryFeeWrapper = dico['entryFeeWrapper']
        if 'periodFeeWrapper' in dico : self.periodFeeWrapper = dico['periodFeeWrapper']
        if 'exitFeeWrapper' in dico : self.exitFeeWrapper = dico['exitFeeWrapper']
        if 'periodProfitTax' in dico : self.periodProfitTax = dico['periodProfitTax']
        if 'finalProfitTax' in dico : self.finalProfitTax = dico['finalProfitTax']
                        
    def Evolution(self, benchmark ) :
        """
        This function returns the value of portfolio as a function of time.
        A simplistic annual model is used.
        """

        return inv.Evolution(
            benchmark.initDeposit
            , benchmark.periodDeposit 
            , self.returnRate 
            , benchmark.nPeriod
            , self.entryFee 
            , self.periodFee 
            , self.exitFee 
            , self.entryFeeWrapper 
            , self.periodFeeWrapper 
            , self.exitFeeWrapper 
            , self.periodProfitTax 
            , self.finalProfitTax 
            )

