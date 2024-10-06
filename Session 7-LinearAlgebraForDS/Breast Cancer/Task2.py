import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean, cityblock, chebyshev

# Load the dataset into a DataFrame
df = pd.read_csv('Breast_cancer_data.csv')

# Extract features and diagnosis column
a1 = df.drop(columns=['diagnosis']).values
diagnosis = df['diagnosis'].values

# Define the second array (ensure it has the same number of features as each row in a1)
a2 = np.array([19.22, 10.01, 125.8, 1021, 0.1284])  # Adjust `a2` if you have more features or include diagnosis if necessary

# Calculate distances and store them with their row indices
distances = []
for i, row in enumerate(a1):
    euclidean_distance = euclidean(row, a2)
    manhattan_distance = cityblock(row, a2)
    chebyshev_distance = chebyshev(row, a2)
    
    distances.append((i, euclidean_distance, manhattan_distance, chebyshev_distance, diagnosis[i]))

# Sort rows by Euclidean distance and select the top 3 nearest rows
distances.sort(key=lambda x: x[1])  # Sorting by Euclidean distance
top_3_distances = distances[:3]

print("Nearest 3 By Euclidean:")
# Print the top 3 rows
for i, euclidean_distance, manhattan_distance, chebyshev_distance, diag in top_3_distances:
    print(f"Row {i+1}:")
    print(f"  Euclidean distance: {euclidean_distance:.4f}")
    print(f"  Manhattan distance: {manhattan_distance:.4f}")
    print(f"  Chebyshev distance: {chebyshev_distance:.4f}")
    print(f"  Diagnosis: {diag}")
    print("\n")
