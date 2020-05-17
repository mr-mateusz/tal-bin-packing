from itertools import permutations
from typing import List, Callable, Tuple

from pympler.asizeof import asizeof

from bin import Bin


def first_fit(elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
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

    memory_taken = asizeof(elements) + asizeof(capacity) + asizeof(bins)
    return elem, memory_taken, [bn.elements for bn in bins]


def last_fit(elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
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

    memory_taken = asizeof(elements) + asizeof(capacity) + asizeof(bins)
    return elem, memory_taken, [bn.elements for bn in bins]


def best_fit(elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
    """Put new object into the fullest bin with enough space."""
    candidate = -1
    candidate_will_be_taken = 0
    will_be_taken = 0

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

    memory_taken = asizeof(elements) + asizeof(capacity) + asizeof(bins) + asizeof(candidate) + asizeof(
        candidate_will_be_taken) + asizeof(will_be_taken)
    return elem, memory_taken, [bn.elements for bn in bins]


def worst_fit(elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
    """Put new object into the emptiest bin with enough space."""
    candidate = -1
    candidate_will_be_taken = 0
    will_be_taken = 0

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

    memory_taken = asizeof(elements) + asizeof(capacity) + asizeof(bins) + asizeof(candidate) + asizeof(
        candidate_will_be_taken) + asizeof(will_be_taken)
    return elem, memory_taken, [bn.elements for bn in bins]


def next_fit(elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
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

    memory_taken = asizeof(elements) + asizeof(capacity) + asizeof(bins)
    return elem, memory_taken, [bn.elements for bn in bins]


def optimal_solution(elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
    """Try next fit for all permutations and take best solution."""
    memory_taken = 0

    elem = 0
    best_sol = [[e] for e in elements]
    for permutation in permutations(elements):
        elem_in_step, memory_taken_in_step, solution = next_fit(permutation, capacity)
        if memory_taken_in_step + asizeof(best_sol) > memory_taken:
            memory_taken = memory_taken_in_step + asizeof(best_sol)
        elem += elem_in_step
        if len(solution) < len(best_sol):
            best_sol = solution

    return elem, memory_taken, best_sol


def decreasing_version(which_one: Callable, elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
    """'Decreasing' versions of algorithms."""
    elements = sorted(elements, reverse=True)
    return which_one(elements, capacity)


def first_fit_decreasing(elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
    return decreasing_version(first_fit, elements, capacity)


def last_fit_decreasing(elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
    return decreasing_version(last_fit, elements, capacity)


def best_fit_decreasing(elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
    return decreasing_version(best_fit, elements, capacity)


def worst_fit_decreasing(elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
    return decreasing_version(worst_fit, elements, capacity)


def next_fit_decreasing(elements: List[int], capacity: int) -> Tuple[int, int, List[List[int]]]:
    return decreasing_version(next_fit, elements, capacity)
