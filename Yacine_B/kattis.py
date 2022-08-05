n, dom = input().split()

score = 0

points = {
    "A": {
        "Dom": 11,
        "Non_Dom": 11,
    },
    "K": {
        "Dom": 4,
        "Non_Dom": 4,
    },
    "Q": {
        "Dom": 3,
        "Non_Dom": 3,
    },
    "J": {
        "Dom": 20,
        "Non_Dom": 2,
    },
    "T": {
        "Dom": 10,
        "Non_Dom": 10,
    },
    "9": {
        "Dom": 14,
        "Non_Dom": 0,
    },
    "8": {
        "Dom": 0,
        "Non_Dom": 0,
    },
    "7": {
        "Dom": 0,
        "Non_Dom": 0,
    },
}

for _ in range(4 * int(n)):
    hand = input()
    score += points[hand[0]]["Dom"] if hand[1] == dom else points[hand[0]]["Non_Dom"]

print(score)
