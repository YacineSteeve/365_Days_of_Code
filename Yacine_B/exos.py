import sys
from itertools import permutations

def change(cash: int) -> dict or None:
	strings = {2: "two", 5: "five", 10: "ten"}
	
	for availables in permutations([10, 5, 2], 3):
		quantities = []
		remainder = cash
		
		for available in availables:
			quantity, remainder = divmod(remainder, available)
			quantities.append((quantity, remainder))
		
		if quantities[-1][1] == 0:
			result = {}
			
			for key, value in zip(availables, quantities):
				result[strings[key]] = value[0]
			
			return result

	return None

print(change(int(sys.argv[1])))

