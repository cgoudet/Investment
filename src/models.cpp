#include "models.h"
#include <algorithm>

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

  double sum = 0;
  for ( unsigned i_asset=0; i_asset<m_assets.size(); ++i_asset ) {
    sum += m_assets[i_asset].get_value()*m_weights[i_asset];
  }
  
  return sum;
}
void Investment::BrokerContract::normalize_weights() {}

void Investment::BrokerContract::process_period( double deposit ) {
  for ( unsigned i_asset=0; i_asset<m_assets.size(); ++i_asset ) {
    m_assets[i_asset].process_period( deposit * m_weights[i_asset] );
  }
}
