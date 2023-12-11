import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

actual_winners = ["Brabham-Repco", "Ferrari", "Williams", "Williams", "Ferrari", "Mercedes","Red Bull"]

# Read the data
years = [1967,1977,1987,1997,2007,2017,2023]
for i in range(1,8):
    data = pd.read_csv('clean_data_period_'+str(i)+'.csv')
    target_year = years[i-1]  # Change the year here

    # Data preparation
    # Remove unnecessary columns if needed
    # Convert categorical variables if necessary
    label_encoder = LabelEncoder()
    data['name_x'] = label_encoder.fit_transform(data['name_x'])
    data['winner'] = (data['positionText'] == 1).astype(int)

    # Update target variable and feature definitions
    features = ['constructorId', 'year', 'name_x', 'relation']
    target_column = 'winner'

    # Split data into training, validation, and test sets
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
    train_data, val_data = train_test_split(train_data, test_size=0.2, random_state=42)

    # Define target variable and features
    X_train = train_data[features]
    y_train = train_data[target_column]

    X_val = val_data[features]
    y_val = val_data[target_column]

    X_test = test_data[features]
    y_test = test_data[target_column]

    # Create and train the model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model accuracy on the validation set
    predictions_val = model.predict(X_val)
    mse_val = mean_squared_error(y_val, predictions_val)
    #print(f'Mean Squared Error on validation set: {mse_val}')

    # Evaluate the model accuracy on the test set
    predictions_test = model.predict(X_test)
    mse_test = mean_squared_error(y_test, predictions_test)
    #print(f'Mean Squared Error on test set: {mse_test}')

    # Predictions on the validation set
    predictions_val_binary = (predictions_val > 0.5).astype(int)
    accuracy_val = accuracy_score(y_val, predictions_val_binary)
    #print(f'Accuracy on validation set: {accuracy_val}')

    # Predictions on the test set
    predictions_test_binary = (predictions_test > 0.5).astype(int)
    accuracy_test = accuracy_score(y_test, predictions_test_binary)
    #print(f'Accuracy on test set: {accuracy_test}')

    # Read the data (replace 'clean_data_period_1.csv' with your data file name)
    all_data = pd.read_csv('clean_data_period_'+str(i)+'.csv')

    # Read constructor data (replace 'all_constructors.csv' with your data file name)
    all_constructors = pd.read_csv('all_constructors.csv')

    # Select the year and necessary columns
    data_for_year = all_data[(all_data['year'] == target_year)][['constructorId', 'year', 'name_x', 'relation']]

    # Create label encoder and transform categorical columns
    label_encoder_name_x = LabelEncoder()
    label_encoder_relation = LabelEncoder()

    all_data['name_x'] = label_encoder_name_x.fit_transform(all_data['name_x'])
    all_data['relation'] = label_encoder_relation.fit_transform(all_data['relation'])

    # Iterate through each constructor/team and make predictions
    predictions = []
    for index, row in data_for_year.iterrows():
        input_data = pd.DataFrame({
            'constructorId': [row['constructorId']],
            'year': [row['year']],
            'name_x': label_encoder_name_x.transform([row['name_x']])[0],
            'relation': label_encoder_relation.transform([row['relation']])[0]
        })

        # Make prediction
        prediction = model.predict(input_data)
        predictions.append({'constructorId': row['constructorId'], 'Prediction': prediction[0]})

    # Sort predictions in descending order and take the first one
    top_prediction = sorted(predictions, key=lambda x: x['Prediction'], reverse=True)[0]

    # Replace constructorId with the corresponding name
    top_constructor_name = all_constructors.loc[all_constructors['constructorId'] == top_prediction['constructorId'], 'name'].values[0]
    top_prediction['constructorName'] = top_constructor_name

    # Return the name and prediction of the highest possible winner
    print(f'Highest possible winner in {target_year} is constructorName: {top_prediction["constructorName"]}, Prediction: {top_prediction["Prediction"]}' + " Actual Winner that year: " + actual_winners[i-1])


