import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.quadratic_poly import *

del sys.path[0]


def test_init_quadratic():
    p = QuadraticPoly([-2, -7, 9])
    q = QuadraticPoly(7, 1, 5)
    r = QuadraticPoly(3, 0, 4)
    
    with pytest.raises(LengthException):
        a = QuadraticPoly([3, -1, 6, 4])
        
    with pytest.raises(LengthException):        
        a = QuadraticPoly(0)
    
    with pytest.raises(TypeError):
        a = QuadraticPoly('string', 5, 1)


p = QuadraticPoly([-2, -7, 9])
q = QuadraticPoly(1, -2, 1)        
r = QuadraticPoly(3, 0, 4)
t = QuadraticPoly(-3, 7, 2)
        
        
def test_coefs():
    assert q.a == 1
    assert q.b == -2
    assert q.c == 1
    assert q.get_coefs() == [q.a, q.b, q.c]


def test_deg():
    assert p.deg == 2
    

def test_cont():
    assert q.const == q.c == 1
    
    
def test_get_determinant():
    assert p.get_determinant() == 121
    assert q.get_determinant() == 0


def test_get_real_roots():
    assert r.get_real_roots() == ()
    assert q.get_real_roots() == (1.0, 1.0)
    assert p.get_real_roots() == (-4.5, 1.0)
    assert t.get_real_roots() == (-0.2573339575529217, 2.590667290886255)
    assert t.get_real_roots(rounded=3) == (-0.257, 2.591)

    with pytest.raises(TypeError):
        r.get_real_roots(rounded='string')
    

def test_get_complex_roots():
    assert q.get_complex_roots() == ()
    assert p.get_complex_roots() == ()
    assert r.get_complex_roots() == (1.1547005383792515j, -1.1547005383792515j)
    assert r.get_complex_roots(rounded=2) == (1.15j, -1.15j)
    
    with pytest.raises(TypeError):
        r.get_complex_roots(rounded='string')
    
    
def test_get_roots():
    assert q.get_roots() == q.get_real_roots()
    assert r.get_roots() == r.get_complex_roots()
    

def test_factors():
    assert p.factors() == ["-2", "x - (-4.5)", "x - (1.0)"]


def test_factorised():
    assert q.factorised() == "(x - (1.0))*(x - (1.0))"
