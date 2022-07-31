x, y, n = map(int, input().split())

for i in range(1, n + 1):
    if i % x == 0:
        if i % y == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % y == 0:
        print("Buzz")
    else:
        print(i)
