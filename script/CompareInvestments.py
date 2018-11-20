import argparse
import json
import os
import sys

sys.path.insert(0, sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))))
from src.Model import InvestModel, InvestBenchmark
import src.Plot as plot

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
    args =ParseArgs()

    benchmark = InvestBenchmark(json.loads(open(args.benchmark).read()))
    
    evols = [ InvestModel(json.loads(open( model).read())).Evolution(benchmark)
              for model in args.configFiles]
    plot.Plot(evols, 'dum.pdf', [plot.StripString(model) for model in args.configFiles] )


if __name__ == '__main__' :
    main()
