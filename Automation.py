import os
from itertools import product

for weights in product(range(2), repeat=9):
    with open("weights.txt", "w") as f:
        for weight in weights:
            f.write(str(weight))

    os.system("make run")

    with open("collisions.txt", "r") as f:
        collisions = f.readline()
    if collisions != 0:
        print(weights)