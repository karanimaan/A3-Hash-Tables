import os
from itertools import product

for weights in product(range(6), repeat=9):
    with open("weights.txt", "r") as f:
        for weight in weights:
            f.write(str(weight))
    os.system("make run")
