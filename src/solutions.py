from itertools import permutations
from typing import List

from src.bin import Bin


def first_fit(elements: List[int], capacity: int) -> List[List[int]]:
    """Put element into first bin with enough space."""
    bins = [Bin()]
    for element in elements:
        for bn in bins:
            if bn.cap_taken + element <= capacity:
                bn.add(element)
                break
        else:
            new_bin = Bin()
            new_bin.add(element)
            bins.append(new_bin)

    return [bn.elements for bn in bins]


def last_fit(elements: List[int], capacity: int) -> List[List[int]]:
    """Put element into last bin with enough space."""
    bins = [Bin()]
    for element in elements:
        for bn in reversed(bins):
            if bn.cap_taken + element <= capacity:
                bn.add(element)
                break
        else:
            new_bin = Bin()
            new_bin.add(element)
            bins.append(new_bin)

    return [bn.elements for bn in bins]


def next_fit(elements: List[int], capacity: int) -> List[List[int]]:
    """Put element into last bin, start new if bin if necessary."""
    bins = [Bin()]
    for element in elements:
        if bins[-1].cap_taken + element <= capacity:
            bins[-1].add(element)
        else:
            new_bin = Bin()
            new_bin.add(element)
            bins.append(new_bin)

    return [bn.elements for bn in bins]


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
