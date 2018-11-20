#define BOOST_TEST_MODULE TESTMODELS
#define BOOST_TEST_DYN_LINK
#include <boost/test/unit_test.hpp>

#include "models.h"
#include <iostream>
using std::cout;
using std::endl;

BOOST_AUTO_TEST_SUITE( TestAsset )
//====================================================
BOOST_AUTO_TEST_CASE( TestAssetConstructor ) {
  Investment::Asset asset;
  asset = Investment::Asset( 1, 0);
}

BOOST_AUTO_TEST_CASE( TestAssetProcessPeriod ) {
  
  Investment::Asset asset( 0.2, 0.1);
  asset.process_period( 100, 0.3, 0.2 );
  BOOST_CHECK_CLOSE( asset.get_value(), 100, 1e-6 );

  asset.process_period( 100, 0.3, 0.2 );
  BOOST_CHECK_CLOSE( asset.get_value(), 204, 1e-6 );

  asset.process_period( 100 );
  BOOST_CHECK_CLOSE( asset.get_value(), 320.32, 1e-6);
  
}

BOOST_AUTO_TEST_SUITE_END()


//====================================================
BOOST_AUTO_TEST_SUITE( TestBrokerContract )
BOOST_AUTO_TEST_CASE( TestBrokerContractConstructor ) {
  Investment::BrokerContract bc;
}

BOOST_AUTO_TEST_CASE( TestBrokerContractAddAsset ) {

  Investment::BrokerContract bc;

  Investment::Asset asset0( 0.2, 0.1);
  Investment::Asset asset1( 0.5, 0.3);

  bc.add_asset( asset0, 1 );
  bc.add_asset( asset1, 2 );

  // Adding negative and 0 weights to check they don't appear
  bc.add_asset( asset1, -1 );
  bc.add_asset( asset1, 0 );

  BOOST_CHECK_EQUAL( bc.size(), 2 );
}

BOOST_AUTO_TEST_CASE( TestBrokerContractProcessPeriod ) {

  Investment::BrokerContract bc;

  Investment::Asset asset0( 0.2, 0);
  Investment::Asset asset1( 0.5, 0);

  bc.add_asset( asset0, 1 );
  bc.add_asset( asset1, 2 );

  bc.process_period( 100 );
  BOOST_CHECK_CLOSE( bc.get_value(), 100, 1e-5);

  bc.process_period( 100 );
  BOOST_CHECK_CLOSE( bc.get_value(), 240, 1e-5 );

}

BOOST_AUTO_TEST_SUITE_END()
