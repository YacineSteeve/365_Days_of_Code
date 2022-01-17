"""
source: https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
"""
from collections import Counter

shoes = int(input())
sizes = Counter(list(map(int, input().split())))
nb_clients = int(input())
s = 0

for client in range(nb_clients):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        sizes[size] -= 1
        s += price

print(s)
