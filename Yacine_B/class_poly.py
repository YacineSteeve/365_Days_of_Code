from itertools import zip_longest


class Poly:
    """ Beautifully manage various lengths and degrees single-variable polynomials.
        Coefficients order should be (an, -->, ao)
        Zero terms should be specified when on the right side."""

    def __init__(self, *coefs):
        self.coefs = list(reversed(coefs))
        self.deg = len(self.coefs) - 1
        self.const = self.coefs[0]

        if not all(map(lambda x: type(x) in [int, float, complex], self.coefs)):
            try:
                raise TypeError
            except TypeError:
                print(f"Polynomial ill instantiated! All of the coefficients should be integer, float or complex.")
                exit()

    def is_const(self):
        """Test whether the polynomial is a constant or not"""
        return len(self.coefs) == 1

    def display(self):
        """Make a display of the polynomial"""
        poly = ""
        for i, a in enumerate(self.coefs):
            if a != 0:
                elem = f"{a}" if type(a) is complex else f"({a})"
                if i == 1:
                    elem += f"x"
                elif i > 1:
                    elem += f"x^{i}"
                poly = elem + poly
                if i != len(self.coefs) - 1:
                    poly = " + " + poly
        print(poly)

    def evaluate(self, x):
        return sum([a * (x ** i) for i, a in enumerate(self.coefs)])

    def __add__(self, other):
        polys = [self.coefs] + [other.coefs]
        return Poly(*reversed([sum(coef) for coef in zip_longest(*polys, fillvalue=0)]))

    def __sub__(self, other):
        polys = [self.coefs] + [other.coefs]
        return Poly(*reversed([coef[0] - coef[1] for coef in zip_longest(*polys, fillvalue=0)]))


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
