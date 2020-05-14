from itertools import permutations
from typing import List, Callable, Tuple

from bin import Bin


def first_fit(elements: List[int], capacity: int) -> Tuple[int, List[List[int]]]:
    """Put element into first bin with enough space."""
    elem = 0
    bins = [Bin()]
    for element in elements:
        for bn in bins:
            elem += 1
            if bn.cap_taken + element <= capacity:
                bn.add(element)
                break
        else:
            new_bin = Bin()
            new_bin.add(element)
            bins.append(new_bin)

    return elem, [bn.elements for bn in bins]


def last_fit(elements: List[int], capacity: int) -> Tuple[int, List[List[int]]]:
    """Put element into last bin with enough space."""
    elem = 0
    bins = [Bin()]
    for element in elements:
        for bn in reversed(bins):
            elem += 1
            if bn.cap_taken + element <= capacity:
                bn.add(element)
                break
        else:
            new_bin = Bin()
            new_bin.add(element)
            bins.append(new_bin)

    return elem, [bn.elements for bn in bins]


def best_fit(elements: List[int], capacity: int) -> Tuple[int, List[List[int]]]:
    """Put new object into the fullest bin with enough space."""
    elem = 0
    bins = [Bin()]
    for element in elements:
        candidate = -1
        candidate_will_be_taken = 0
        for index, bn in enumerate(bins):
            will_be_taken = bn.cap_taken + element
            elem += 1
            if candidate_will_be_taken < will_be_taken <= capacity:
                candidate = index
                candidate_will_be_taken = will_be_taken
        if candidate != -1:
            bins[candidate].add(element)
        else:
            new_bin = Bin()
            new_bin.add(element)
            bins.append(new_bin)

    return elem, [bn.elements for bn in bins]


def worst_fit(elements: List[int], capacity: int) -> Tuple[int, List[List[int]]]:
    """Put new object into the emptiest bin with enough space."""
    elem = 0
    bins = [Bin()]
    for element in elements:
        candidate = -1
        candidate_will_be_taken = capacity + 1  # to ensure that first bin that will be full will be taken
        for index, bn in enumerate(bins):
            will_be_taken = bn.cap_taken + element
            elem += 1
            if will_be_taken < candidate_will_be_taken:
                candidate = index
                candidate_will_be_taken = will_be_taken
        if candidate != -1:
            bins[candidate].add(element)
        else:
            new_bin = Bin()
            new_bin.add(element)
            bins.append(new_bin)

    return elem, [bn.elements for bn in bins]


def next_fit(elements: List[int], capacity: int) -> Tuple[int, List[List[int]]]:
    """Put element into last bin, start new if bin if necessary."""
    elem = 0
    bins = [Bin()]
    for element in elements:
        elem += 1
        if bins[-1].cap_taken + element <= capacity:
            bins[-1].add(element)
        else:
            new_bin = Bin()
            new_bin.add(element)
            bins.append(new_bin)

    return elem, [bn.elements for bn in bins]


def optimal_solution(elements: List[int], capacity: int) -> Tuple[int, List[List[int]]]:
    """Try next fit for all permutations and take best solution."""
    elem = 0
    best_sol = [[e] for e in elements]
    for permutation in permutations(elements):
        elem_in_step, solution = next_fit(permutation, capacity)
        elem += elem_in_step
        if len(solution) < len(best_sol):
            best_sol = solution

    return elem, best_sol


def decreasing_version(which_one: Callable, elements: List[int], capacity: int) -> Tuple[int, List[List[int]]]:
    """'Decreasing' versions of algorithms."""
    elements = sorted(elements, reverse=True)
    return which_one(elements, capacity)