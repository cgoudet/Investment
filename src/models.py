"""
Components of an investment stategy
"""


class Asset(object) :
    "Contrat wrapping financial assets together"

    def __init__( self, constant_rate = 0
                  , constant_fee = 0 ) :
        """
        :param float constant_rate: growing rate per period of the asset
        :param float constant_fee: periodic fee of the asset
        """
        self.constant_rate = constant_rate
        self.constant_fee = constant_fee

        self.values = []
        
    def process_period( self, deposit=0
                        , rate = None
                        , fee = None ) :
        """ 
        Update the contract by one period

        :param float deposit: deposit on the contract for the period
        :param float rate: interest rate of the period
        :param float fee: periodic fee of the period
        """
        if rate is None : rate = self.constant_rate
        if fee is None : fee = self.constant_fee

        if not len(self.values) : self.values = [ deposit ]
        else : self.values.append( self.values[-1] * (1+rate) * (1-fee) + deposit )
        
        return self.values[-1]

    def reset( self ) :
        """ Reset the contract prior to the first deposit
        """
        self.values=[]

        
