vowels = 'aeiou'
s = input().lower()
count = 0

for v in vowels:
    count += s.count(v)

print(count)
