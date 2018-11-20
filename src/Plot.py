import matplotlib.pyplot as plt
import numpy as np

def StripString( line, doPrefix = 1, doSuffix = 1 ) :
    if ( line.rfind( '.' ) != -1 and doSuffix ) : line = line[0:line.rfind( '.' )]
    if ( line.rfind( '/' ) != -1 and doPrefix ) : line = line[line.rfind( '/' )+1:len( line )]
    return line

#==========
def Plot( data, outName, legends, x=None ) :

    if x is None : x = range(len(data[0] ))
    plt.figure()
    for i, vals in enumerate(data) : plt.plot(x, vals)
    plt.legend(legends)
    plt.xlabel('Period')
    plt.ylabel('Value')
    plt.tight_layout()
    plt.savefig(outName)
