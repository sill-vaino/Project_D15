import pandas as pd

# data
clean_data = pd.read_csv('clean_data.csv')

# Making three separate data segments
period_1 = clean_data[clean_data['year'].between(1958, 1976)]
period_2 = clean_data[clean_data['year'].between(1977, 1995)]
period_3 = clean_data[clean_data['year'].between(1996, 2023)]

# Creating new data files:
period_1.to_csv('clean_data_period_1.csv', index=False)
period_2.to_csv('clean_data_period_2.csv', index=False)
period_3.to_csv('clean_data_period_3.csv', index=False)

