for _ in range(int(input())):
    s = input()
    to = s.find("Simon says ")
    if to != -1:
        print(s[11:])
