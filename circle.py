__author__ = 'mamoon'
from pylab import *

from geom_formulae import *

v_circle_area = np.vectorize(circle_area)
#v__square_perimeter = np.vectorize(circle_perimeter)

R = np.linspace(0,10) # our side lengths

A = v_circle_area(R)  # the areas
#P = v_square_perimeter(S)  # the perimeters

plot(R, A, '-r', label="Area")
#plot(S, P, ':b', label="Perimeter")

xlabel('side length')
ylabel('geo values')
title('Square Geo Properties')
legend(loc='upper right')

show()