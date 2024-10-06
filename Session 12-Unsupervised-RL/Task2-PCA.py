import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load your dataset
df = pd.read_csv('real_2016_air.csv')

# Select features to be used for PCA
features = ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5']
X = df[features]

# 1. Standardize the Data
# calculate the mean and standard deviation of each feature in the feature space.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert scaled data back to a DataFrame for easier handling
df_scaled = pd.DataFrame(X_scaled, columns=features)

# 2. Calculate Covariance Matrix
cov_matrix = np.cov(df_scaled.T)  # Transpose to get features as rows
print('Covariance Matrix:\n', cov_matrix)

# 3. Compute Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Print eigenvalues and eigenvectors
print('Eigenvalues:\n', eigenvalues)
print('Eigenvectors:\n', eigenvectors)

# 4. Select Principal Components
# Sort eigenvalues and eigenvectors
eigenvalue_index = np.argsort(eigenvalues)[::-1]  # Sort in descending order
eigenvalues_sorted = eigenvalues[eigenvalue_index]
eigenvectors_sorted = eigenvectors[:, eigenvalue_index]

# Choose the number of principal components (e.g., top 2)
num_components = 2
selected_eigenvectors = eigenvectors_sorted[:, :num_components]

print('Selected Eigenvectors (Principal Components):\n', selected_eigenvectors)

# 5. Transform the Data
# Project the original data onto the principal components
X_pca = np.dot(X_scaled, selected_eigenvectors)

# Convert PCA result to DataFrame for easier handling
df_pca = pd.DataFrame(X_pca, columns=[f'PC{i+1}' for i in range(num_components)])

print('Transformed Data:\n', df_pca.head())
