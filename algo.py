import pandas as pd
import entropy_hT
import entropy_hTe

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

def predict_next_day(stock_data):
    data_partitions_6 = create_finite_partition(data2023, 6)
    data_partitions_5 = create_finite_partition(data2023, 5)
    data_partitions_4 = create_finite_partition(data2023, 4)
    data_partitions_3 = create_finite_partition(data2023, 3)
    data_partitions_2 = create_finite_partition(data2023, 2)

    entropy_data = entropy_hT.calculate_entropy_hT(stock_data)
    entropy_partition_6 = entropy_hTe.calculate_limit_entropy(stock_data, data_partitions_6)
    entropy_partition_5 = entropy_hTe.calculate_limit_entropy(stock_data, data_partitions_5)
    entropy_partition_4 = entropy_hTe.calculate_limit_entropy(stock_data, data_partitions_4)
    entropy_partition_3 = entropy_hTe.calculate_limit_entropy(stock_data, data_partitions_3)
    entropy_partition_2 = entropy_hTe.calculate_limit_entropy(stock_data, data_partitions_2)

    entropy_partition_mean = (entropy_partition_6+entropy_partition_5+entropy_partition_4+entropy_partition_3+entropy_partition_2)/5


    return entropy_partition_mean < entropy_data**2




stock_data = pd.read_csv('spx.csv')
sorted_data = stock_data.sort_values(by='Date')
finite_partition = sorted_data['Close'].tolist()

closing_price_partitions = create_finite_partition(finite_partition, 1500)
data2023 = closing_price_partitions[1498]

print(predict_next_day(data2023))
