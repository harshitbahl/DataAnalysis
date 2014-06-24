# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 22:00:19 2014

@author: harshitbahl
"""
import scipy
import numpy
import sys
import matplotlib.pyplot
def main():
    if(len(sys.argv) != 3):
       print "Usage python %s yfactor xfactor" % (sys.argv[0])
       sys.exit()
    
    # Loads the Lena image into an array
    lena = lena = scipy.imag('/Users/harshitbahl/Pictures/IMG_1550 1.JPG')
    #Lena's dimensions
    LENA_X = 512
    LENA_Y = 512
    #Check the shape of the Lena array
#    numpy.testing.assert_equal((LENA_X, LENA_Y), lena.shape)
    
    # Get the resize factors
    yfactor = float(sys.argv[1])
    xfactor = float(sys.argv[2])
    
    # Resize the Lena array
    resized = lena.repeat(yfactor, axis=0).repeat(xfactor, axis=1)
    
    #Check the shape of the resized array
    numpy.testing.assert_equal((yfactor * LENA_Y, xfactor * LENA_Y), resized.shape)
    
    # Plot the Lena array
    matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.imshow(lena)
    
    #Plot the resized array
    matplotlib.pyplot.subplot(212)
    matplotlib.pyplot.imshow(resized)
    matplotlib.pyplot.show()

    
    





if __name__ == '__main__':
    main()