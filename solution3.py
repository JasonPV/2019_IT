import numpy as np
import math
def get_indices(N, n_batches, split_ratio):
    """Generates splits of indices from 0 to N-1 into uniformly distributed\
       batches. Each batch is defined by 3 indices [i, j, k] where\
       (j-i) = split_ratio*(k-j). The first batch starts with i = 0,\
       the last one ends with k = N - 1.
    Args:
        N (int): total counts
        n_batches (int): number of splits
        split_ratio (float): split ratio, defines position of j in [i, j, k].
    Returns:
        generator for batch indices [i, j, k]
    """
    length = (N - 1) // (n_batches + (1/split_ratio))
    inds = np.array([0, 0, 0])

    for i in range(n_batches):
        inds[1] = inds[0] + length * (1 / split_ratio)
        inds[2] = inds[1] + length
        yield list(map(math.floor, inds))
        inds[0] += length


def main():
    for inds in get_indices(100, 5, 0.25):
        print(inds)
    # expected result:
    # [0, 44, 55]
    # [11, 55, 66]
    # [22, 66, 77]
    # [33, 77, 88]
    # [44, 88, 99]

if __name__ == "__main__":
    main()