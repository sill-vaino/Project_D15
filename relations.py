import pandas as pd

# Load data from "constructors.csv" file
constructors_data = pd.read_csv('constructors.csv')

# Define categories for teams
mclaren = [1, "McLaren", "McLaren-Serenissima", "McLaren-Ford", "McLaren-Alfa Romeo"]
williams = [3, "Williams", "Williams-BMW", "Williams-Renault", "Williams-Ford", "Williams-Mercedes"]
renault = [4, "Renault", "Alpine F1 Team", "Renault-Lotus", "Lotus F1 Team"]
toro_rosso = [5, "Toro Rosso", "AlphaTauri"]
lotus = [7, "Lotus-Climax", "Lotus", "Lotus F1 Team", "Lotus-Maserati", "Lotus-Pratt & Whitney"]
spyker = [8, "Spyker", "MF1", "Spyker MF1"]
marussia = [9, "Marussia", "Manor Marussia"]
aston_martin = [10, "Aston Martin", "Racing Point", "Force India"]
sauber = [11, "Sauber", "Alfa Romeo", "Sauber-Petronas"]
cooper = [12, "Cooper", "Cooper-Maserati", "Cooper-OSCA", "Cooper-Borgward", "Cooper-Climax",
          "Cooper-Castellotti", "Cooper-Alfa Romeo", "Cooper-Ford", "Cooper-Ferrari", "Cooper-ATS", "Cooper-BRM"]
shadow = [13, "Shadow", "Shadow-Ford", "Shadow-Matra"]
brabham = [14, "Brabham", "Brabham-Alfa Romeo", "Brabham-BRM", "Brabham-Climax", "Brabham-Ford", "Brabham-Repco"]
deTomaso = [15, "De Tomaso", "De Tomaso-Alfa Romeo", "De Tomaso-Ferrari", "De Tomaso-Osca"]
lds = [16, "LDS", "LDS-Alfa Romeo", "LDS-Climax"]
eagle = [17, "Eagle", "Eagle-Climax", "Eagle-Weslake"]
march = [18, "March", "March-Alfa Romeo", "March-Ford"]

# Collect all team categories into one list
formula_teams = [march, eagle, lds, deTomaso, brabham, shadow, cooper, sauber, aston_martin, marussia, spyker, lotus, toro_rosso, renault, williams, mclaren]

# Add a new ID to each constructor based on the category
constructors_data['new_constructorId'] = constructors_data.apply(lambda row: next((team[0] for team in formula_teams if row['name'] in team), None), axis=1)

# If the constructor was not found, assign it a unique ID
constructors_data['new_constructorId'].fillna(constructors_data['constructorId'], inplace=True)

# Create a new column "relation"
constructors_data['relation'] = constructors_data['new_constructorId'].astype(int)

# Create a new "all_constructors.csv" file
all_constructors_data = constructors_data[['constructorId', 'name', 'nationality', 'relation']]
all_constructors_data.to_csv('all_constructors.csv', index=False)

