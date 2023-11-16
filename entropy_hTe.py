import itertools
import math

# Calculates the limit entropy by iterating over all possible combinations of indices representing subsets in the partition. 
# It computes the intersection probabilities of the sequence with these subsets, multiplies them, and accumulates in sum_entropy.
def calculate_limit_entropy(sequence, partition):
    n = len(partition)
    sum_entropy = 0

    for combination in itertools.product(range(n), repeat=n):
        intersection_prob = 1
        for subsetIndex in range(n):
            subset = partition[combination[subsetIndex]]
            intersection_prob *= len(set(sequence).intersection(set(subset))) / n

        sum_entropy += intersection_prob * math.log(intersection_prob)

    return -sum_entropy / n

# sequence = [1, 2, 3, 4, 5]
# finite_partition = [[1, 2], [3, 4, 5]]
# limit_entropy = calculate_limit_entropy(sequence, finite_partition)
# print(f"The limit entropy for the sequence {sequence} with the given partition is: {limit_entropy}")