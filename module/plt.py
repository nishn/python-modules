#!/usr/bin/env python
# coding: UTF-8

import sys
import exceptions

import module as m

try:
    import numpy as np
    import matplotlib.pyplot as plt
except:
    sys.exit( 'error : To use hist, you need to install "numpy" and "matplotlib" module first.' )


@m.set_type( **{ 'data'            : list,
                 'outfilename'     : str,
                 'nbins'           : int,
                 'y2lab'           : str,
                 'with_cumulative' : bool  } )
def norm_hist( data, outfilename = 'hist.png', nbins = 10, y2lab = 'Cumulative Curve', with_cumulative = True, **kwargs ):

    histdata = plt.hist( data, nbins, **kwargs )
    # clear figure buffer
    plt.clf()

    # prepare plot
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    # plot histgram
    ax1.bar( histdata[1][0:-1], histdata[0] / sum( histdata[0] ),
             width = (max(histdata[1]) - min(histdata[1]))/ len(histdata[0]), color = 'cyan' )

    if 'xlab' in kwargs.keys():
        ax1.set_xlabel( xlab )
    if 'ylab' in kwargs.keys():
        ax1.set_ylabel( ylab )
    if 'title' in kwargs.keys():
        ax1.set_title( title )
    if 'xlim' in kwargs.keys():
        ax1.set_xlim( xlim )
    if 'ylim' in kwargs.keys():
        ax1.set_ylim( ylim )
    

    # plot cumulative curve
    if with_cumulative:
        # set 2nd plot
        ax2 = ax1.twinx()
        ax2.set_ylabel( y2lab )

        # get cumulative data
        cumudata = plt.hist( data, nbins, cumulative = True )
        plt.clf()

        midpoint = [ (cumudata[1][i] + cumudata[1][i+1]) / 2.0 for i in range( len( cum[1] ) - 1 ) ]
        ax2.plot( midpoint, cum[0]/cum[0][-1], 'b.-', linewidth=2 )

    plt.savefig( outfilename )
    plt.clf()
    
def norm_cumu
