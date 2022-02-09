import pytest
from ..src import poly


p = poly.Poly(-5, 0, 4, -2, 1+2j, 7)
q = poly.Poly([5, 3, 0, -1])


def test_init():
    q = poly.Poly([5, 3, 0, -1])

    with pytest.raises(TypeError):
        raise TypeError
