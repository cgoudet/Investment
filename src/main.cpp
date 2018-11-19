#include <iostream>
#include "models.h"

using std::cout;
using std::endl;

int main() {
  cout << "Hello World!" << endl;
  Investment::Asset asset;
  asset.process_period( 100, 0, 0 );
  asset.process_period( 100, 0.1, 0 );
  cout << asset.get_value() << endl;
   
  return 0;
  
}
