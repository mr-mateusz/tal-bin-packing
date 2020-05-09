from itertools import permutations
from typing import List


def first_fit(elements: List[int], capacity: int) -> List[List[int]]:
    """Put element into first bin with enough space."""
    bins = [[]]
    taken_caps = [0]
    for element in elements:
        for i, bn in enumerate(bins):
            if taken_caps[i] + element <= capacity:
                taken_caps[i] += element
                bn.append(element)
                break
        else:
            bins.append([element])
            taken_caps.append(element)
    return bins


def next_fit(elements: List[int], capacity: int) -> List[List[int]]:
    """Put element into last bin, start new if bin if necessary."""
    bins = [[]]
    for element in elements:
        if sum(bins[-1]) + element <= capacity:
            bins[-1].append(element)
        else:
            bins.append([element])
    return bins


def best_fit():
    pass


def optimal_solution(elements: List[int], capacity: int) -> List[List[int]]:
    """Try next fit for all permutations and take best solution."""
    best_sol = [[e] for e in elements]
    for permutation in permutations(elements):
        solution = next_fit(permutation, capacity)
        if len(solution) < len(best_sol):
            best_sol = solution
    return best_sol
