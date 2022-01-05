from poly import Poly
from math import sqrt


class MyExceptions(Exception):
    pass


class LengthException(MyExceptions):
    pass


class QuadraticPoly(Poly):
    def __init__(self, *coefs):
        if type(coefs[0]) is list:
            super().__init__(*coefs[0])
        else:
            super().__init__(*coefs)

        if self.deg > 2:
            raise LengthException("Too much coefficients! A quadratic polynomial has at most 3 coefficients.")

        self.a, self.b, self.c = self.get_coefs()

    def get_determinant(self):
        return self.b**2 - 4 * self.a * self.c

    def real_roots(self, rounded=None):
        delta = self.get_determinant()
        if delta >= 0:
            s1 = (- self.b + sqrt(delta)) / (2 * self.a)
            s2 = (- self.b - sqrt(delta)) / (2 * self.a)
            if not rounded:
                return s1, s2
            else:
                return round(s1, rounded), round(s2, rounded)
        else:
            return None

    def complex_roots(self, rounded=None):
        delta = self.get_determinant()
        if delta < 0:
            real_part = - self.b / (2 * self.a)
            im_part = sqrt(abs(delta)) / (2 * self.a)
            if rounded:
                real_part, im_part = round(real_part, rounded), round(im_part, rounded)
            return complex(real_part, im_part), complex(real_part, -im_part)
        else:
            return None

    def get_roots(self, rounded=None):
        c = self.complex_roots(rounded=rounded)
        r = self.real_roots(rounded=rounded)
        if not c:
            return r
        elif not r:
            return c

    def factors(self):
        an = [str(self.a)] if self.a != 1 else []

        for root in self.get_roots(rounded=1):
            fact = f"x + {-root}" if type(root) is complex else f"x + ({-root})"
            an.append(fact)
        return an

    def factorised(self):
        return ''.join([f"({fact})" for fact in self.factors()])
    
