import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data (replace 'clean_data.csv' with your data file name)
data = pd.read_csv('clean_data.csv')

# Specify the number of periods (10 years per period)
years_per_period = 10
total_years = data['year'].max() - data['year'].min() + 1
periods = total_years // years_per_period + (total_years % years_per_period > 0)

# Split the data into periods
data_periods = []
for i in range(periods):
    start_year = data['year'].min() + i * years_per_period
    end_year = start_year + years_per_period - 1
    period_data = data[(data['year'] >= start_year) & (data['year'] <= end_year)]
    data_periods.append(period_data)

# Add all remaining data to the last period
data_periods[-1] = pd.concat(data_periods[-1:], ignore_index=True)

# Save each period as a separate CSV file
for i, period_data in enumerate(data_periods):
    period_data.to_csv(f'clean_data_period_{i + 1}.csv', index=False)

# Display the size of each period
for i, period_data in enumerate(data_periods):
    print(f"Size of Period {i + 1} data: {len(period_data)}")
