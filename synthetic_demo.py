"""Deterministic DTW demonstration using artificial signals only.

This file never reads the private participant data or historical result caches.
Its output is a software check, not evidence about authentication performance.
"""

from math import inf, pi, sin


def dtw_distance(left, right):
    """Return classic unnormalized Dynamic Time Warping distance."""
    previous = [inf] * (len(right) + 1)
    previous[0] = 0.0
    for left_value in left:
        current = [inf] * (len(right) + 1)
        for index, right_value in enumerate(right, start=1):
            cost = abs(left_value - right_value)
            current[index] = cost + min(current[index - 1], previous[index], previous[index - 1])
        previous = current
    return previous[-1]


def artificial_signal(phase, scale=1.0, samples=100):
    return [scale * sin((2 * pi * index / samples) + phase) for index in range(samples)]


def main():
    reference = artificial_signal(0.0)
    similar = artificial_signal(0.08)
    different = artificial_signal(1.1, scale=0.65)
    similar_distance = dtw_distance(reference, similar)
    different_distance = dtw_distance(reference, different)
    assert similar_distance < different_distance
    print(f"synthetic similar distance: {similar_distance:.6f}")
    print(f"synthetic different distance: {different_distance:.6f}")
    print("check passed: similar artificial signal has the smaller DTW distance")


if __name__ == "__main__":
    main()
