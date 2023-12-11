import pandas as pd

# Loading data
constructor_results = pd.read_csv('constructor_results.csv')
all_constructors = pd.read_csv('all_constructors.csv')
constructor_standings = pd.read_csv('constructor_standings.csv')
races = pd.read_csv('races.csv')

# Merging data
merged_data = pd.merge(constructor_results, all_constructors, on='constructorId', how='inner')
merged_data = pd.merge(merged_data, constructor_standings, on=['raceId', 'constructorId'], how='inner')
merged_data = pd.merge(merged_data, races, on='raceId', how='inner')

# Selecting desired columns
clean_data = merged_data[['constructorId', 'year', 'name_x', 'positionText', 'relation']]

# Sorting data
clean_data = clean_data.sort_values(by='year')

# Displaying and saving the result
print(clean_data.head(20))
clean_data.to_csv('clean_data.csv', index=False)


