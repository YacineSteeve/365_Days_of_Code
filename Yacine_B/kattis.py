given = list(map(int, input().split()))
pos, *code = given

dial = [i for i in range(40)]


def f(x):
    return x * 360 // 40


while any(map(lambda x: x != 0, given)):
    deg = 3 * f(40)

    for index in range(len(code)):
        k = dial.index(pos)
        while dial[k % len(dial)] != code[index]:
            if index in [0, 2]:
                k -= 1
            else:
                k += 1
            deg += f(1)
        pos = code[index]

    print(deg)

    given = list(map(int, input().split()))
    pos, *code = given
