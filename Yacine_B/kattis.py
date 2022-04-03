for _ in range(int(input())):
    n, *grades = map(int, input().split())

    average = sum(grades) / n

    above = list(filter(lambda x: x > average, grades))

    percentage = round(100 * len(above) / n, 3)

    if percentage == int(percentage):
        percentage = str(percentage) + '00'

    print(percentage, '%', sep='')
