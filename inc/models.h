#ifndef MOLDELS_H
#define MODELS_H

#include <vector>

namespace Investment {

  /**\brief Single financial asset
   */
  class Asset {

  public:

    Asset( double constant_rate=0, double constant_fee=0 );
    double get_value() { return m_values.back(); };
    void process_period( double deposit=0, double rate=-1, double fee=-1 ); // -1 triggers real default value
    void reset() { m_values.clear(); };
    
  private:
    
    double m_constant_rate;
    double m_constant_fee;

    std::vector<double> m_values;
  };


  /**\brief Contract wrapping multiple assets, with own fee
   */
  class BrokerContract {
  public :
    double get_value();
    void process_period( double deposit );
    void normalize_weights();
    void add_asset( Asset asset, double weight );
    
  private :
    double m_periodic_fee;
    double m_entry_fee;
    double m_exit_fee;

    std::vector<Asset> m_assets;
    std::vector<double> m_weights;
  };
}
#endif
