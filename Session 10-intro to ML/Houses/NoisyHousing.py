import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

# Load and clean the data
housing = pd.read_csv("housingNoisy.csv")
housing_cleaned = housing.drop_duplicates()

def fill_missing_values(data):
    data.iloc[:, :] = data.iloc[:, :].replace(0, np.nan)
    imputer = SimpleImputer(strategy='mean')
    data.iloc[:, :8] = imputer.fit_transform(data.iloc[:, :8])
    
    mode_value = data.iloc[:, 9].mode()
    if not mode_value.empty:
        mode_value = mode_value[0]
        
        # Get unique values excluding the mode
        values_to_replace = data.iloc[:, 9].dropna().unique()
        values_to_replace = [val for val in values_to_replace if val != mode_value]

        # Fill NaN values with the mode value
        data.iloc[:, 9].fillna(mode_value, inplace=True)
        
        # Replace specific values with the mode value
        data.iloc[:, 9] = data.iloc[:, 9].replace(values_to_replace, mode_value)
        
    return data

# Fill missing values and store cleaned data
housing_cleaned = fill_missing_values(housing_cleaned)
housing_cleaned.to_csv("housing_cleaned.csv", index=False)

def IQRSample(data):
    # Calculate Q1, Q3, and IQR
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [x for x in data if x <= lower_bound or x >= upper_bound]
    
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Outliers  based on IQR:", outliers)
    # return outliers

def CalcZscore():
    column_of_interest = housing_cleaned.iloc[:, 5] 
    filled = column_of_interest.dropna()
    
    mean_score = np.mean(filled)
    std_dev = np.std(filled)
    z_scores = [(x - mean_score) / std_dev for x in filled]
    
    threshold = 2
    outliers_z = [x for x, z in zip(filled, z_scores) if abs(z) > threshold]
    
    # print("Z-Scores:", z_scores)
    print("Outliers based on Z-scores:", outliers_z)
    
    # Plot the data
    # plt.scatter(np.arange(len(filled)), filled)
    # plt.xlabel('Index')
    # plt.ylabel('Values')
    # plt.title('Scatter Plot of Data')
    # plt.show()

# Example usage
IQRSample(housing_cleaned.iloc[:, 5])  # Use a specific column of interest for IQR sampling
CalcZscore()
