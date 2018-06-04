import argparse
import json
import os
import sys

sys.path.insert(0, sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))))

import src.Plot as plot
import src.Cost as cost


def ParseArgs() :
    parser = argparse.ArgumentParser()
    parser.add_argument( 'configFiles', nargs='+', type=str )
    parser.add_argument( '--benchmark', type=str )
    args = parser.parse_args()

    #testing file existence
    for f in args.configFiles :
        if not os.path.exists(f) : raise RuntimeError( 'File {} does not exist.'.format(f ))
    if not os.path.exists(args.benchmark) : raise RuntimeError( 'File {} does not exist.'.format(args.benchmark))

    return args

#==========
def main() :
    maxVal=10000
    costs = [ cost.Cost( c, maxVal=maxVal )  for c in [[(2.5, 1000), (5,3000), (10, 7692), (0.0013,100000)]
                                        , [(0.99,500), (1.9,1000), (2.90,2000), (3.8, 4400), (0.0009,100000)]
                                                       , [(1.95, 500), (3.9, 2000), (0.002, 1000000)]]
    ]

    print(costs)
    plot.Plot(costs, 'cost.pdf', ['BForBank', 'BourseDirect', 'Fortuneo'], x=range(0, maxVal+1, 100) )
    
if __name__ == '__main__' :
    main()
