import unittest
import numpy as np
from .. import models

class TestAsset(unittest.TestCase):

    def test_constructor(self) :
        models.Asset()
        models.Asset( 1, 1 )
        models.Asset( constant_rate=0.2, constant_fee=0.1 )

    def test_process_period(self) :
        asset = models.Asset( constant_rate=0.02, constant_fee=0.01 )
        self.assertEqual( [], asset.values )

        self.assertEqual( asset.process_period( deposit=100, rate=0, fee=0 ), 100 )
        self.assertEqual( [100], asset.values )

        # test the sum of previous + new value
        self.assertEqual( asset.process_period( deposit=100, rate=0, fee=0 ), 200 )
        self.assertEqual( [100, 200], asset.values )

        # test interest rate
        self.assertEqual( asset.process_period( deposit=0, rate=0.02, fee=0 ), 204 )
        self.assertAlmostEqual( asset.process_period( deposit=0, rate=0, fee=0.01 ), 201.96 )

    def test_reset(self) :
        asset = models.Asset()
        asset.process_period()
        self.assertEqual( len(asset.values), 1 )

        asset.reset()
        self.assertEqual( len(asset.values), 0 )


class TestBrokerContract( unittest.TestCase ) :

    def test_constructor(self) :
        models.BrokerContract()
        models.BrokerContract( 1, 1, 1)
        models.BrokerContract( entry_fee=1, periodic_fee=1, exit_fee=1)

    def test_normalize_weights(self) :
        bc = models.BrokerContract( entry_fee=0.2 )

        # test no crash
        bc.normalize_weights()

        # test single entry 
        bc.add_asset( models.Asset(), 0.5 )
        bc.normalize_weights()
        np.testing.assert_array_equal( bc.assets['weight'].values, [1])

        # test mutliple entries
        bc.add_asset( models.Asset(), 1 )
        bc.normalize_weights()
        np.testing.assert_array_equal( bc.assets['weight'].values, [0.5, 0.5])


    def test_add_asset( self ) :
        bc = models.BrokerContract( entry_fee=0.2 )

        bc.add_asset( models.Asset(), 0 )
        self.assertEqual( len(bc.assets), 0 )

        bc.add_asset( models.Asset(), -1 )
        self.assertEqual( len(bc.assets), 0 )

        bc.add_asset( models.Asset(), 0.2 )
        self.assertEqual( len(bc.assets), 1 )
        self.assertAlmostEqual( bc.assets['weight'].sum(), 0.2 )

        bc.add_asset( models.Asset(), 0.5 )
        self.assertEqual( len(bc.assets), 2 )
        self.assertAlmostEqual( bc.assets['weight'].sum(), 0.7 )
