import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

# Load and clean the data
salaries = pd.read_csv("salariesNoisy.csv")
salaries_cleaned = salaries.drop_duplicates()

def fill_missing_values(data):
    data.iloc[:, :] = data.iloc[:, :].replace(0, np.nan)

    imputer = SimpleImputer(strategy='mean')
    data.iloc[:, [3,5, 6]] = imputer.fit_transform(data.iloc[:, [3,5,6]])
    
    for col in [1, 2, 4]:
        mode_value = data.iloc[:, col].mode()
        if not mode_value.empty:
            mode_value = mode_value[0]  # Take the first mode if multiple modes exist
            data.iloc[:, col].fillna(mode_value, inplace=True)
            values_to_replace = ['Any', 'NONE']  # Add more values as needed
            data.iloc[:, col] = data.iloc[:, col].replace(values_to_replace, mode_value)
    return data

# Fill missing values and store cleaned data
salaries_cleaned = fill_missing_values(salaries_cleaned)
salaries_cleaned.to_csv("salaries_cleaned.csv", index=False)

def IQRSample(data):
    # Calculate Q1, Q3, and IQR
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [x for x in data if x <= lower_bound or x >= upper_bound]
    # print("Dataset:", data)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Outliers based on IQR:", outliers)
    # return outliers

def CalcZscore():
    column_of_interest = salaries_cleaned.iloc[:, 5]  # Example column, adjust as needed
    filled = column_of_interest.dropna()  # Drop NaN values for outlier detection
    
    mean_score = np.mean(filled)
    std_dev = np.std(filled)
    z_scores = [(x - mean_score) / std_dev for x in filled]
    
    threshold = 2
    # Identify outliers based on Z-scores
    outliers_z = [x for x, z in zip(filled, z_scores) if abs(z) > threshold]
    
    # Print results
    # print("Z-Scores:", z_scores)
    print("Outliers based on Z-scores:", outliers_z)
    
    # Plot the data
    # plt.scatter(np.linspace(min(filled), max(filled), len(filled)), filled)
    # plt.xlabel('Index')
    # plt.ylabel('Values')
    # plt.title('Scatter Plot of Data')
    # plt.show()

# Example usage
IQRSample(salaries_cleaned.iloc[:, 5])  # Use a specific column of interest for IQR sampling
CalcZscore()
