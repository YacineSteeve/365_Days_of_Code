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
    
    
def test_sub():
    assert (p - r).is_null()
    assert q - t == q
    assert q - k == Poly(5, 5, 8, -10)
    
    
def test_check_other():
    p._check_other(Poly(4))
    
    with pytest.raises(TypeError):
        p._check_other(4)
    
    
def test_check_root():
    assert k.check_root(1) == True
    assert q.check_root(7) == False
    
    with pytest.raises(TypeError):
        q.check_root('string')