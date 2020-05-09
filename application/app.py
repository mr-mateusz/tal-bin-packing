import random
from itertools import permutations

# elements = [random.randint(1, 5) for _ in range(11)]

bin_size = 10

elements = [9, 7, 6, 5, 1, 3, 4, 2, 1, 2]

random.shuffle(elements)

print(elements)

best_sol = None
for elements in permutations(elements):
    bins = [[]]
    for element in elements:
        if sum(bins[-1]) + element <= bin_size:
            bins[-1].append(element)
        else:
            bins.append([element])
    if best_sol is None or len(bins) < len(best_sol):
        best_sol = bins

print(best_sol)
