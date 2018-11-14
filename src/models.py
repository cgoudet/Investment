"""
Components of an investment stategy
"""
import math

import pandas as pd

from collections import namedtuple


class Asset(object) :
    

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

        
class BrokerContract(object) :
    "Contrat wrapping financial assets together"

    def __init__(self, periodic_fee=0, entry_fee=0, exit_fee=0 ) :

        self.periodic_fee = periodic_fee
        self.entry_fee = entry_fee
        self.exit_fee = exit_fee
        
        self.assets = pd.DataFrame([], columns=['asset', 'weight'] )

    def process_period(self) :
        pass

    def normalize_weights( self ) :
        """
        Change the asset weight so that they sum to one
        """
        if not len(self.assets) : return


        sum_weights = sum( x.weight for x in self.assets )
        if math.isclose(sum_weights, 1) : return 
        self.assets = [  namedtuple( 'Portfolio', ['asset', 'weight'], (asset, weight/sum_weights)  ) for asset, weight in self.assets ]
    
    def add_asset( self, asset, weight ) :
        """ Add an Asset to the portfolio
        :param Asset asset: Asset to be added
        :param float weight: relative weight of the asset for deposit

        Weights of all assets are normalized before any deposit
        """

        if weight <= 0 : return

        frame = pd.DataFrame([[ asset, weight]], columns=['asset', 'weight'])
        self.assets = self.assets.append( frame )

        
