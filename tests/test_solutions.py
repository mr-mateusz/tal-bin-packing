from math import ceil

from src.solutions import next_fit, optimal_solution, first_fit, last_fit

to_test = [9, 7, 6, 1, 4, 3]
cap = 10


def test_first_fit():
    assert first_fit(to_test, cap) == [[9, 1], [7, 3], [6, 4]]


def test_last_fit():
    assert last_fit(to_test, cap) == [[9], [7], [6, 1], [4, 3]]


def test_next_fit():
    assert next_fit(to_test, cap) == [[9], [7], [6, 1], [4, 3]]


def test_optimal_solution():
    optimal = optimal_solution(to_test, cap)
    assert len(optimal) == ceil(sum(to_test) / cap)
