from itertools import zip_longest, product


class MyExceptions(Exception):
    pass


class IntegrationLimitError(Exception):
    pass


class Poly:
    """ Beautifully manage various lengths and degrees single-variable polynomials.
        Coefficients order should be (an, -->, ao).
        Zero terms should be specified when they are not the endpoints of the polynomial.
    """
    
    def __init__(self, *coefs):
        if not coefs:
            raise IndexError("No coefficient found!")
        elif type(coefs[0]) is list:
            self.__coefs = list(reversed(coefs[0]))
        else:
            self.__coefs = list(reversed(coefs))

        if not all(map(lambda x: type(x) in [int, float, complex], self.__coefs)):
            raise TypeError("Polynomial ill instantiated! The coefficients should be integer, float or complex.")
        
        self.deg = len(self.__coefs) - 1
        self.const = self.__coefs[0]

    def is_const(self):
        return self.deg == 0

    def is_null(self):
        return all(map(lambda a: a==0, self.get_coefs()))

    def get_coefs(self):
        return list(reversed(self.__coefs))

    def evaluate(self, x):
        if type(x) not in [int, float, complex]:
           raise TypeError("x must be integer, float or complex!")
        
        terms = [a * (x ** i) for i, a in enumerate(self.__coefs)]
        
        return sum(terms)

    def derivative(self, order=None):
        if order is None:
            order = 1
        else:
            if type(order) is not int or order >= 1:
                raise TypeError("The order of derivation must be integer and greater than 1.")

        new_coefs = self.__coefs
        for _ in range(order):
            new_coefs = [a * i for i, a in enumerate(new_coefs)][1:]
        if not new_coefs:
            return Poly(0)
        return Poly(*reversed(new_coefs))

    def primitive(self, condition=None, rounded=None):
        if condition is None:
            x, y = 0, 0
        else:
            if type(condition) is not tuple or len(condition) != 2:
               raise ValueError("condition must be a couple of two values, (x, p(x))!")
            x, y = condition

            if type(x) not in [int, float] or type(y) not in [int, float]:
                raise TypeError("condition values must be integers or float!")
            
        if rounded is None:
            rounded = True
        
        prim_coefs = [1.0]
        
        for i, a in enumerate(self.__coefs):
            if rounded:
                if type(a) is complex:
                    a = complex(round(a.real / (i + 1), 2), round(a.imag / (i + 1), 2))
                else:
                    a = round(a / (i + 1), 2)
            else:
                if type(a) is complex:
                    a = complex(a.real / (i + 1), a.imag / (i + 1))
                else:
                    a = a / (i + 1)
                
            prim_coefs.append(a)

        c = y - (Poly(*reversed(prim_coefs)).evaluate(x) - 1.0)

        return Poly(*reversed([c] + prim_coefs[1:]))

    def integral(self, x1=None, x2=None):
        if x1 is None and x2 is None:
            x1, x2 = 0, 1
        elif x1 is None or x2 is None:
            raise IntegrationLimitError("Missing one limit of integration.")
        else:
            if type(x1) not in [int, float] or type(x2) not in [int, float]:
                raise TypeError("integration limits must be integers or float!")

        prim = self.primitive(rounded=False)
        return prim.evaluate(x2) - prim.evaluate(x1)

    def check_root(self, x):
        if type(x) not in [int, float, complex]:
            raise TypeError("x must be integer, float or complex!")
        return self.evaluate(x) == 0
    
    def _check_other(self, other):
        if type(other) is not Poly:
            raise TypeError("other must be a Poly() object!")
        
    def __str__(self):
        poly = ""
        if self.is_null():
            return "(0)"
        else:
            for i, a in enumerate(self.__coefs):
                if a != 0:
                    elem = f"{a}" if type(a) is complex else f"({a})"
                    if i == 1:
                        elem += f"x"
                    elif i > 1:
                        elem += f"x^{i}"
                    poly = elem + poly
                    if i != self.deg:
                        poly = " + " + poly
                else:
                    if i == self.deg:
                        poly = poly[3:]
            return poly

    def __getitem__(self, i):
        return self.__coefs[i]
    
    def __eq__(self, other):
        self._check_other(other)
        return self.__coefs == other.__coefs

    def __add__(self, other):
        self._check_other(other)
        polys = [self.__coefs] + [other.__coefs]
        return Poly(*reversed([sum(coef) for coef in zip_longest(*polys, fillvalue=0)]))

    def __sub__(self, other):
        self._check_other(other)
        polys = [self.__coefs] + [other.__coefs]
        return Poly(*reversed([coef[0] - coef[1] for coef in zip_longest(*polys, fillvalue=0)]))

    def __mul__(self, other):
        self._check_other(other)
        prod_deg = 2 * max(self.deg, other.deg)
        prods = list(product(range(prod_deg // 2 + 1), repeat=2))
        part_prod_coefs = [list(filter(lambda tp: sum(tp) == k, prods)) for k in range(prod_deg)]

        prod_coefs = []
        for coef in part_prod_coefs:
            if other.deg < self.deg:
                new_coefs = other.__coefs + [0 for _ in range(self.deg - other.deg)]
                prod_coefs.append(sum([self.__coefs[tp[0]] * new_coefs[tp[1]] for tp in coef]))
            elif self.deg < other.deg:
                new_coefs = self.__coefs + [0 for _ in range(other.deg - self.deg)]
                prod_coefs.append(sum([new_coefs[tp[0]] * other.__coefs[tp[1]] for tp in coef]))
            else:
                prod_coefs.append(sum([self.__coefs[tp[0]] * other.__coefs[tp[1]] for tp in coef]))

        return Poly(*reversed(prod_coefs))

