import os
from itertools import product
from statistics import mean

i = 1
collisions_list = []
for weights in product((5, 4, 3), repeat=9): # options are changed
    with open("weights.txt", "w") as f:
        for weight in weights:
            f.write(str(weight) + "\n")

    os.system("	java -cp bin TestHashTable 0 > /dev/null")

    with open("collisions.txt", "r") as f:
        collisions = int(f.readline())
    if collisions == 0:
        with open("correct_weights.txt", "a") as f:
            f.write(str(weights) + "\n")

    collisions_list.append(collisions)
    print("%-10s %-30s %-10s %d" % (round(i/5**9 *100, ndigits=5), weights, collisions, mean(collisions_list)))
    i+=1

with open("correct_weights.txt", "r") as f:
    print(f.readlines())