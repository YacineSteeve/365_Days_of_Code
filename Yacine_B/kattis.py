import re

smiles = [r":\)", r";\)", r":-\)", r";-\)"]
string = input()

indices = sorted([match.start(0)for smile in smiles for match in re.finditer(smile, string)])

print(*indices, sep='\n')
