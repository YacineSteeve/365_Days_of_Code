for _ in range(int(input())):
    s1, s2 = input(), input()
    print(s1)
    print(s2)
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            print('.', end='')
        else:
            print('*', end='')
    print()
