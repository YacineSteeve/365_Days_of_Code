
def alnum(s):
    for c in s:
        if c.isalnum():
            return True
    return False


def alpha(s):
    for c in s:
        if c.isalpha():
            return True
    return False


def digit(s):
    for c in s:
        if c.isdigit():
            return True
    return False


def lower(s):
    for c in s:
        if c.islower():
            return True
    return False


def upper(s):
    for c in s:
        if c.isupper():
            return True
    return False


if __name__ == '__main__':
    s = input()
    print(alnum(s))
    print(alpha(s))
    print(digit(s))
    print(lower(s))
    print(upper(s))
