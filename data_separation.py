import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data (replace 'clean_data.csv' with your data file name)
data = pd.read_csv('clean_data.csv')

# Set the number of periods
periods = 4

# Split the data into periods
data_periods = []
for i in range(periods):
    start_idx = i * len(data) // periods
    end_idx = (i + 1) * len(data) // periods
    period_data = data.iloc[start_idx:end_idx]
    data_periods.append(period_data)

# Save each period as a separate CSV file
for i, period_data in enumerate(data_periods):
    period_data.to_csv(f'clean_data_period_{i + 1}.csv', index=False)

# Show the size of each period
for i, period_data in enumerate(data_periods):
    print(f"Number of data points in Period {i + 1}: {len(period_data)}")
