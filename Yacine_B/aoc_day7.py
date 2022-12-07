# 😭😭 Not workiiiiiiing 💔!!!!

import re
from collections import defaultdict

tree_pattern = '\$ cd ([a-z]+?)\$ ls(.*?)\$ cd \.\.'
dir_pattern = 'dir ([a-z]+)(?:\$|dir|\d|$)'
file_pattern = '[\d]+? ([a-z.]+)(?:\$|dir|\d|$)'

root = {
    'plws': [],
    'pwlbgbz': [],
    'pwtpltr': [],
    'szn': []
}

matches = defaultdict(list)
    
    
with open('input.txt', 'r') as file:
    data = ''.join(list(map(lambda l: l.strip(), file.readlines())))


    def parse(directory):
        print(directory)
        ms = re.findall(tree_pattern, data)
        if ms:
            for m in ms:
                if m[0] == directory:
                    fs = re.findall(file_pattern, m[1])
                    if fs:
                        for f in fs:
                            matches[directory].append(f)
                    ds = re.findall(dir_pattern, m[1])
                    if ds:
                        for d in ds:
                            parse(ds)
    
    for el in root.keys():
        parse(el)
    
    print(matches)
