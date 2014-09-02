__author__ = 'mamoon'
from geom_formulae import*
from nose.tools import*


def test_square_area_int():
    assert square_area(1) == 1
    assert square_area(4) == 16
    s = 5
    assert square_area(s*2) == 4*square_area(s)


eps = 1e-6
def test_square_area_double():
    assert 25/4 - eps < square_area(2.5) < 25/4 + eps

def test_fail_square_perimeter():
    assert square_perimeter(4) == 20


def test circle_area_int():
    assert circle_area(1) == 1
    assert circle_area(4) == 16
    s = 5
    assert circle_area(s*2) == 4*square_area(s)


eps = 1e-6
def test_circle_area_double():
    assert 25/4 - eps < circle_area(2.5) < 25/4 + eps

def test_fail_circle_perimeter():
    assert circle_perimeter(4) == 20
