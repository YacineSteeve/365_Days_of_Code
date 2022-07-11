import random


def pi_approx(pts: list) -> float:

	# For any point (x, y) inside a circle of radius r centered to (0, 0), we have x² + y² < r², where x² + y² is its squared distance to zero.
	
	squared_distances_to_zero = [item[0]**2 + item[1]**2 for item in pts]
	
	distances_inside_circle = list(filter(lambda d: d < 1, squared_distances_to_zero))
	
	# proba = pi / 4 = len(pts_inside) / len(pts)
	
	approx = 4 * len(distances_inside_circle) / len(pts)
	
	return approx
	
	
rands= []

for i in range(100000):
	arr = [random.random(), random.random()]
	rands.append(arr)

print(pi_approx(rands))

