from itertools import zip_longest, product


class MyExceptions(Exception):
    pass


class IntegrationLimitError(Exception):
    pass


class Poly:
    """
    Beautifully manage various lengths and degrees single-variable polynomials.
    Coefficients order should be (an, -->, ao)
    Zero terms should be specified when they are not the endpoints of the polynomial.
    """

    def __init__(self, *coefs):
        if type(coefs[0]) is list:
            self.__coefs = list(reversed(coefs[0]))
        else:
            self.__coefs = list(reversed(coefs))

        self.deg = len(self.__coefs) - 1
        self.const = self.__coefs[0]

        if not all(map(lambda x: type(x) in [int, float, complex], self.__coefs)):
            raise TypeError(f"Polynomial ill instantiated! The coefficients should be integer, float or complex.")

    def is_const(self):
        """
        Test whether the polynomial is a constant or not
        :return: Boolean
        """
        return self.deg == 0

    def is_null(self):
        """
        Whether the polynomial is the K-Zero polynomial.
        :return: Boolean
        """
        return self.deg == 0 and self.const == 0

    def get_coefs(self):
        return list(reversed(self.__coefs))

    def evaluate(self, x):
        """Calculate the polynomial for a given value x"""
        terms = [a * (x ** i) for i, a in enumerate(self.__coefs)]
        if not terms:
            return 0
        return sum(terms)

    def derivative(self, order=None):
        """
        Generate the derivative at the order _order_ of the polynomial.
        :return: Polynomial (object Poly)
        """
        if order is None:
            order = 1

        new_coefs = self.__coefs
        for _ in range(order):
            new_coefs = [a * i for i, a in enumerate(new_coefs)][1:]
        if not new_coefs:
            return Poly(0)
        return Poly(*reversed(new_coefs))

    def primitive(self, condition=None):
        if condition is None:
            x, y = 0, 0
        else:
            x, y = condition

        prim_coefs = [1.0]

        for i, a in enumerate(self.__coefs):
            if type(a) is complex:
                a = complex(round(a.real / (i + 1), 2), round(a.imag / (i + 1), 2))
            else:
                a = round(a / (i + 1), 2)
            prim_coefs.append(a)

        c = y - (Poly(*reversed(prim_coefs)).evaluate(x) - 1.0)

        return Poly(*reversed([c] + prim_coefs[1:]))

    def integral(self, x1=None, x2=None):
        if x1 is None and x2 is None:
            x1, x2 = 0, 1
        elif x1 is None or x2 is None:
            raise IntegrationLimitError("Missing one limit of integration.")

        prim = self.primitive()
        return prim.evaluate(x2) - prim.evaluate(x1)

    def test_root(self, x):
        """
        :param x: Float or Integer.
        :return: Boolean
        """
        return self.evaluate(x) == 0

    def __str__(self):
        """
        Make a display of the polynomial.
        :return: String
        """
        poly = ""
        if self.is_null():
            return f"({0})"
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

    def __eq__(self, other):
        return self.__coefs == other.__coefs

    def __getitem__(self, item):
        return self.__coefs[item]

    def __add__(self, other):
        polys = [self.__coefs] + [other.__coefs]
        return Poly(*reversed([sum(coef) for coef in zip_longest(*polys, fillvalue=0)]))

    def __sub__(self, other):
        polys = [self.__coefs] + [other.__coefs]
        return Poly(*reversed([coef[0] - coef[1] for coef in zip_longest(*polys, fillvalue=0)]))

    def __mul__(self, other):
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


if __name__ == "__main__":
    p = Poly(-5, 0, 4, -2, 1 + 2j, 7)
    q = Poly([5, 3, 0, -1])

    print(p.primitive())
    print(q.integral(1, 2))
