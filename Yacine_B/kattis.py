game = ["ball", "empty", "empty"]


def move_a(cups):
    cups[0], cups[1] = cups[1], cups[0]


def move_b(cups):
    cups[1], cups[2] = cups[2], cups[1]


def move_c(cups):
    cups[0], cups[2] = cups[2], cups[0]


moves = {
    "A": move_a,
    "B": move_b,
    "C": move_c
}

for move in input():
    moves[move](game)

for i, cup in enumerate(game):
    if cup == "ball":
        print(i+1)
