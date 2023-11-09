from itertools import combinations
from math import log2 

def calculate_entropy_hT(sequence):
    max_entropy = float('-inf')
    n = len(sequence)
    for partition_size in range(1, n + 1):
        for partition_combination in combinations(sequence, partition_size):
            partition = list(partition_combination)
            entropy = calculate_partition_entropy(partition)

            max_entropy = max(max_entropy, entropy)

    return max_entropy

def calculate_partition_entropy(partition):
    probabilities = [partition.count(element) / len(partition) for element in set(partition)]
    entropy = -sum(p * log2(p) for p in probabilities if p > 0)
    return entropy

sequence = [1, 2, 3, 4, 5]
sequence2 = [1, 1, 1, 1, 1, 4, 5]

print(f"The entropy of the sequence {sequence} is: {calculate_entropy_hT(sequence)} and partition entropy is: {calculate_partition_entropy(sequence)}")
print(f"The entropy of the sequence {sequence2} is: {calculate_entropy_hT(sequence2)} and partition entropy is: {calculate_partition_entropy(sequence2)}")

