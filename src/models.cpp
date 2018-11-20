#include <algorithm>
#include <numeric>
#include <iostream>

#include "models.h"

using std::cout;
using std::endl;

Investment::Asset::Asset( double constant_rate, double constant_fee ) {
  m_constant_rate = std::max(constant_rate, 0.);
  m_constant_fee = std::max(constant_fee, 0.);
}

void Investment::Asset::process_period( double deposit, double rate, double fee ) {

  rate = ( rate < 0 ) ? m_constant_rate : rate;
  fee = ( fee < 0 ) ? m_constant_fee : fee;
    
  if ( !m_values.size() ) m_values.push_back( deposit );
  else m_values.push_back( deposit + m_values.back() * (1+rate) * (1-fee) );
}

//========================
void Investment::BrokerContract::add_asset( Investment::Asset asset, double weight ) {
  if (weight <= 0) return ;
  m_assets.push_back( asset );
  m_weights.push_back( weight );
}

double Investment::BrokerContract::get_value() {

  double sum = std::accumulate( m_assets.begin(), m_assets.end(), 0.
				, []( double current_sum, Investment::Asset &asset ) { return current_sum + asset.get_value(); } );
  return sum;
}

void Investment::BrokerContract::normalize_weights() {
  double total_weight = std::accumulate( m_weights.begin(), m_weights.end(), 0. );
  std::transform( m_weights.begin(), m_weights.end(), m_weights.begin(), [&]( float v ) { return v/total_weight; } );
}

void Investment::BrokerContract::process_period( double deposit ) {
  normalize_weights();
  for ( unsigned i_asset=0; i_asset<m_assets.size(); ++i_asset ) {
    m_assets[i_asset].process_period( deposit * m_weights[i_asset] );
  }
}
