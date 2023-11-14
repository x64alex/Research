import pandas as pd
import entropy_hT

# Create a partition based on consecutive dates
def create_finite_partition(data, num_partitions):
    points_per_partition = len(data) // num_partitions

    consecutive_partitions = []

    for i in range(num_partitions):
        start_index = i * points_per_partition
        end_index = (i + 1) * points_per_partition
        if type(data) == list:
            partition = data[start_index:end_index]
        else:
            partition = data.iloc[start_index:end_index]
        consecutive_partitions.append(partition)

    return consecutive_partitions


stock_data = pd.read_csv('spx.csv')
sorted_data = stock_data.sort_values(by='Date')
finite_partition = sorted_data['Close'].tolist()

closing_price_partitions = create_finite_partition(sorted_data, 20)
closing_price_partitions2 = create_finite_partition(finite_partition, 1500)


# print(finite_partition)

# first_partition_close_df = pd.DataFrame({'Close': finite_partition[0]})
# print(type(first_partition_close_df))
# print(closing_price_partitions[0], closing_price_partitions2[0])
# print(len(closing_price_partitions[0]), len(closing_price_partitions2[0]))
print(closing_price_partitions2[18],len(closing_price_partitions2[18]))
print(entropy_hT.calculate_entropy_hT(closing_price_partitions2[18]))