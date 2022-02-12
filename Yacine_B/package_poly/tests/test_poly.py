import pytest
import sys, os

sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.poly import *

del sys.path[0]


p = Poly(-5, 0, 4, -2, 1+2j, 7)
q = Poly([5, 3, 1, -1])
r = Poly([-5, 0, 4, -2, 1+2j, 7])
s = Poly(-3+4j)
t = Poly([0])
k = Poly([-2, -7, 9])


def test_init():
    with pytest.raises(IndexError):
        a = Poly()
        
    with pytest.raises(TypeError):
        a = Poly([5, 3, '4', -1])
    
    with pytest.raises(TypeError):
        a = Poly([5, (3, 0), 4, -1])
        
    with pytest.raises(TypeError):
        a = Poly([[5, 19], 3, 4, -1])
        
    with pytest.raises(TypeError):
        a = Poly([5, True, 4, -1])
        
        

def test_is_const():
    assert p.is_const() == False
    assert s.is_const() == True
    
    
def test_is_null():
    assert p.is_null() == False
    assert t.is_null() == True


def test_get_coefs():
    assert p.get_coefs() == [-5, 0, 4, -2, 1+2j, 7]
    
    
def test_evaluate():
    assert q.evaluate(-1) == -4
    
    with pytest.raises(TypeError):
        q.evaluate('string')

def test_getitem():
    assert q[2] ==  3
    
    
def test_eq():
    assert (p == q) == False
    assert (p == r) == True
    
    
def test_add():
    assert p + q == Poly(-5, 0, 9, 1, 2+2j, 6)
    assert p + q == q + p
    assert (p + q).deg <= max(p.deg, q.deg)
    
    
def test_sub():
    assert (p - r).is_null()
    assert q - t == q
    assert q - k == Poly(5, 5, 8, -10)
    assert (q - k).deg <= max(q.deg, k.deg)

    
    
def test_check_other():
    p._check_other(Poly(4))
    
    with pytest.raises(TypeError):
        p._check_other(4)
    
    
def test_check_root():
    assert k.check_root(1) == True
    assert q.check_root(7) == False
    
    with pytest.raises(TypeError):
        q.check_root('string')
        
        
def test_derivative():
    assert q.derivative() == Poly(15, 6, 1)
    assert q.derivative(1) == q.derivative()
    assert s.derivative() == Poly(0)
    
    with pytest.raises(TypeError):
        a = q.derivative('string')
    with pytest.raises(TypeError):
        a = q.derivative([64])
    with pytest.raises(ValueError):
        a = q.derivative(-2)
        
        
def test_str():
    assert k.__str__() == "(-2)x^2 + (-7)x + (9)"
    assert t.__str__() == "(0)"
        
    a = Poly(0, 4, -1, 12)
    assert a.__str__() == "(4)x^2 + (-1)x + (12)"
  
        
def test_mul():
    assert q * k == Poly(-10, -41, 22, 22, 16, -9)
    assert k * q == q * k
    assert (q * k).deg <= q.deg + k.deg


def test_pow():
    assert k**0 == k
    assert k**2 == k * k == Poly(28, 13, -126, 81)
    
    with pytest.raises(TypeError):
        a = k**'string'
    with pytest.raises(TypeError):
        a = k**[6, '2']    
    with pytest.raises(ValueError):
        a = k**(-4)