import random
from typing import List


def generate_data(n: int, max_capacity: int) -> List[int]:
    return [random.randint(1, max_capacity) for _ in range(n)]


def cumulate(probabilities: List) -> List:
    probabilities = sorted(probabilities, key=lambda x: x[0])
    s = 0
    cumulated = []
    for number, prob in probabilities:
        s += prob
        cumulated.append((number, s))
    return cumulated


def inverse(val: float, probabilities: List) -> int:
    for number, prob in probabilities:
        if val <= prob:
            return number


def inverse_transform_sampling(n: int, probabilities: List) -> List[int]:
    """Generate random numbers using inverse transform sampling.

    Args:
        n: Number of samples
        probabilities: Probability distribution - Iterable of pairs (value, probability)

    Returns:
        List of generated values

    """
    if sum([p[1] for p in probabilities]) != 1:
        raise ValueError("Invalid distribution")

    probabilities = cumulate(probabilities)
    return [inverse(random.uniform(0, 1), probabilities) for _ in range(n)]
