import numpy as np

from src.generator import cumulate, inverse


def test_cumulate():
    to_test = [[2, 0.1], [3, 0.2], [5, 0.2], [7, 0.3], [8, 0.1], [9, 0.1]]
    expected = [[2, 0.1], [3, 0.3], [5, 0.5], [7, 0.8], [8, 0.9], [9, 1]]
    assert np.allclose(cumulate(to_test), expected)


def test_inverse():
    probs = [[2, 0.1], [3, 0.3], [5, 0.5], [7, 0.8], [8, 0.9], [9, 1]]
    assert inverse(0, probs) == 2
    assert inverse(0.05, probs) == 2
    assert inverse(0.1, probs) == 2
    assert inverse(0.111111, probs) == 3
    assert inverse(0.15, probs) == 3
    assert inverse(0.3, probs) == 3
    assert inverse(0.5, probs) == 5
    assert inverse(0.6, probs) == 7
    assert inverse(0.8, probs) == 7
    assert inverse(0.81, probs) == 8
    assert inverse(0.9, probs) == 8
    assert inverse(0.91, probs) == 9
    assert inverse(0.96, probs) == 9
    assert inverse(1, probs) == 9
