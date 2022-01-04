from itertools import zip_longest, product


class Poly:
    """
    Beautifully manage various lengths and degrees single-variable polynomials.
    Coefficients order should be (an, -->, ao)
    Zero terms should be specified when on the right side.
    """

    def __init__(self, *coefs):
        if type(coefs[0]) is list:
            self.__coefs = list(reversed(coefs[0]))
        else:
            self.__coefs = list(reversed(coefs))

        self.deg = len(self.__coefs) - 1
        self.const = self.__coefs[0]

        if not all(map(lambda x: type(x) in [int, float, complex], self.__coefs)):
            try:
                raise TypeError
            except TypeError:
                print(f"Polynomial ill instantiated! All of the coefficients should be integer, float or complex.")
                exit()

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

    def display(self):
        """
        Make a display of the polynomial.
        :return: None
        """
        poly = ""
        if self.is_null():
            print(f"({0})")
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
            print(poly)

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
        if not order:
            order = 1

        new_coefs = self.__coefs
        for _ in range(order):
            new_coefs = [a * i for i, a in enumerate(new_coefs)][1:]
        if not new_coefs:
            return Poly(0)
        return Poly(*reversed(new_coefs))

    def test_root(self, x):
        """
        :param x: Float or Integer.
        :return: Boolean
        """
        return self.evaluate(x) == 0
    
    def __getitem__(self, item):
        return self.__coefs[item]

    def __add__(self, other):
        polys = [self.__coefs] + [other.coefs]
        return Poly(*reversed([sum(coef) for coef in zip_longest(*polys, fillvalue=0)]))

    def __sub__(self, other):
        polys = [self.__coefs] + [other.coefs]
        return Poly(*reversed([coef[0] - coef[1] for coef in zip_longest(*polys, fillvalue=0)]))

    def __mul__(self, other):
        prod_deg = self.deg + other.deg + 1
        prods = list(product(range(prod_deg//2 + 1), repeat=2))
        part_prod_coefs = [list(filter(lambda tp: tp[0] + tp[1] == k, prods)) for k in range(prod_deg)]

        if other.deg < self.deg:
            new_coefs = other.coefs + [0 for _ in range(self.deg - other.deg)]
            prod_coefs = [sum([self.__coefs[tp[0]] * new_coefs[tp[1]] for tp in coef]) for coef in part_prod_coefs]
        elif self.deg < other.deg:
            new_coefs = self.__coefs + [0 for _ in range(other.deg - self.deg)]
            prod_coefs = [sum([new_coefs[tp[0]] * other.coefs[tp[1]] for tp in coef]) for coef in part_prod_coefs]
        else:
            prod_coefs = [sum([self.__coefs[tp[0]] * other.coefs[tp[1]] for tp in coef]) for coef in part_prod_coefs]

        return Poly(*reversed(prod_coefs))

if __name__ == "__main__":
    p = Poly(-5, 0, 4, -2, 1+2j, 7)
    q = Poly(5, 3, 0, -1)
    t = Poly(4, 0)
    r = Poly(7)

    # Some test cases.

    p.display()
    print()
    print(p.deg)
    print(q.const)
    print()
    s = p + q
    print(s.coefs)
    s = p - q
    s.display()
    print(p.evaluate(2))
    print()
    print(t.is_const())
    t.display()
    print()
    print(r.is_const())
    r.display()
