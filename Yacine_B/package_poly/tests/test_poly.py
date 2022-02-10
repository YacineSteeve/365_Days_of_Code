import pytest
import sys, os

sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.poly import *

del sys.path[0]





def test_init_with_string():
    with pytest.raises(TypeError):
        q = Poly([5, 3, '4', -1])
        
def test_init_with_tuple():
    with pytest.raises(TypeError):
        q = Poly([5, (3, 0), 4, -1])
        
def test_init_with_list():
    with pytest.raises(TypeError):
        q = Poly([[5, 19], 3, 4, -1])
        
def test_init_with_bool():
    with pytest.raises(TypeError):
        q = Poly([5, True, 4, -1])
        

def test_is_const():
    p = Poly(-5, 0, 4, -2, 1+2j, 7)
    q = Poly(-3+4j)
    assert p.is_const() == False
    assert q.is_const() == True
    
    
def test_is_null():
    p = Poly([-5, 0, 4, -2, 1+2j, 7])
    q = Poly([0])
    assert p.is_null() == False
    assert q.is_null() == True


def test_get_coefs():        
    p = Poly(-5, 0, 4, -2, 1+2j, 7)
    assert p.get_coefs() == [-5, 0, 4, -2, 1+2j, 7]
    
    
def test_evaluate():
    q = Poly([5, 3, 4, -1])
    assert q.evaluate(-1) == -7


def test_getitem():
    q = Poly([5, 3, 4, -1])
    assert q[2] ==  3
    
    
def test_eq():
    p = Poly(-5, 0, 4, -2, 1+2j, 7)
    q = Poly([5, 3, 4, -1])
    r = Poly([-5, 0, 4, -2, 1+2j, 7])
    assert (p == q) == False
    assert (p == r) == True