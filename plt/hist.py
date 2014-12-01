#!/usr/bin/env python
# coding: UTF-8

import sys
import exceptions

import module

try:
    import numpy as np
    import matplotlib.pyplot as plt
except:
    sys.exit( 'error : To use hist, you need to install "numpy" and "matplotlib" module first.' )


@set_type( **{ 'data'            : list,
               'outfilename'     : str,
               'title'           : str,
               'nbins'           : int,
               'xlab'            : str,
               'ylab'            : str,
               'y2lab'           : str,
               'with_cumulative' : bool  } )
def histgram( data, outfilename = 'hist.png', nbins = 10, title = 'title',
              xlab = 'x', ylab = 'y', y2lab = 'Cumulative Curve', with_cumulative = True, **kwargs ):

    histdata = plt.hist( data, nbins )
    cumudata = plt.hist( data, nbins, cumulative = True )
    # clear figure buffer
    plt.clf()

    # prepare plot
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    # plot histgram
    ax1.bar( histdata[1][0:-1], hist[0] / sum( hist[0] ),
             width = (max(hist[1]) - min(hist[1]))/ len(hist[0]), color = 'cyan' )

    ax1.set_xlabel( xlab )
    ax1.set_ylabel( ylab )
    ax1.set_title( title )
    ax1.set_xlim( [] )
    ax1.set_ylim( [] )
    
