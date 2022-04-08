import re

n = int(input())

guests = ''.join(input().split())

langs = list(set(guests))

if all(map(lambda x: guests.count(x) == 1, langs)):
    print(n)
else:
    awks = []

    for lang in langs:
        digits = '0123456789'.replace(lang, '')
        pattern = lang + '[' + digits + ']*(?=' + lang + ')'

        where = re.findall(pattern, guests)

        awk = [len(w) for w in where if w]

        if awk:
            awks.append(min(awk))

    print(min(filter(lambda x: x != 0, awks)))
