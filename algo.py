import pandas as pd

# Create a partition based on consecutive dates
def create_partition(data, num_partitions=500):
    sorted_data = data.sort_values(by='Date')

    points_per_partition = len(data) // num_partitions

    consecutive_partitions = []

    for i in range(num_partitions):
        start_index = i * points_per_partition
        end_index = (i + 1) * points_per_partition
        partition = sorted_data.iloc[start_index:end_index]
        consecutive_partitions.append(partition)

    return consecutive_partitions


stock_data = pd.read_csv('spx.csv')
closing_price_partitions = create_partition(stock_data, 5000)

print("First Partition:", closing_price_partitions[4800])
