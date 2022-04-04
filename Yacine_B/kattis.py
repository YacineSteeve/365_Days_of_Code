grid = [list(map(int, input().split())) for _ in range(4)]

direction = int(input())

# 0: left
# 1: up
# 2: right
# 3: down


def slide_lr(side: int) -> None:
    for i in range(4):
        new_row = []
        grid[i] = list(filter(lambda x: x != 0, grid[i]))

        while grid[i]:
            g = [grid[i].pop(side)]
            if grid[i] and grid[i][side] == g[side]:
                g.append(grid[i].pop(side))

            if side == -1:
                new_row.insert(0, sum(g))
            else:
                new_row.append(sum(g))

        while len(new_row) < 4:
            if side == -1:
                new_row.insert(0, 0)
            else:
                new_row.append(0)

        grid[i] = new_row


def transpose(matrix: list) -> list:
    new_matrix = []

    for i in range(4):
        new_row = []
        for j in range(4):
            new_row.append(matrix[j][i])
        new_matrix.append(new_row)

    return new_matrix


if direction == 0:
    slide_lr(0)
elif direction == 1:
    grid = transpose(grid)
    slide_lr(0)
    grid = transpose(grid)
elif direction == 2:
    slide_lr(-1)
elif direction == 3:
    grid = transpose(grid)
    slide_lr(-1)
    grid = transpose(grid)
else:
    print("Unknown direction.")

for row in grid:
    print(*row)
