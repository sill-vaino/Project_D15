import pandas as pd

# Loading Data
constructor_results = pd.read_csv('constructor_results.csv')
constructors = pd.read_csv('constructors.csv')
constructor_standings = pd.read_csv('constructor_standings.csv')
races = pd.read_csv('races.csv')

# Connecting data
merged_data = pd.merge(constructor_results, constructors, on='constructorId', how='inner')
merged_data = pd.merge(merged_data, constructor_standings, on=['raceId', 'constructorId'], how='inner')
merged_data = pd.merge(merged_data, races, on='raceId', how='inner')

# Choosing columns
clean_data = merged_data[['name_y', 'year', 'name_x', 'positionText']]

# Naming columns
clean_data = clean_data.rename(columns={'name_y': 'race_name', 'name_x': 'constructor_name'})
# Sorting my new data
clean_data = clean_data.sort_values(by='year')


# testing
print(clean_data.head(20))

clean_data.to_csv('clean_data.csv', index=False)


