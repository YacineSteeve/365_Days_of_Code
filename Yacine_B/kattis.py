speeds = []
photos = [tuple(map(int, input().split())) for _ in range(int(input()))]

for i in range(1, len(photos)):
    time = photos[i][0] - photos[i-1][0]
    distance = photos[i][1] - photos[i - 1][1]
    speeds.append(distance // time)

print(max(speeds))
