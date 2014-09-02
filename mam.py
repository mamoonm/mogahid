__author__ = 'mamoon'
from pylab import *

from geom_formulae import *

v_rectangle_area = np.vectorize(rectangle_area)
#v__square_perimeter = np.vectorize(square_perimeter)

S = np.linspace(0,10) # our side lengths

L = v_square_area(S)  # the areas
W = 2

plot(S, A, '-r', label="Area")
plot(S, P, ':b', label="Perimeter")

xlabel('side length')
ylabel('geo values')
title('Square Geo Properties')
legend(loc='upper right')

show()