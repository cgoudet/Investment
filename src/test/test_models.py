import unittest

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


