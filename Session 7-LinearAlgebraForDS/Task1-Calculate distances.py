import numpy as np
from scipy.spatial.distance import euclidean, cityblock, chebyshev

# Define the arrays
a1 = np.array([
    [51, 92, 14, 71, 60], 
    [20, 82, 86, 74, 70], 
    [10, 84, 70, 33, 61], 
    [75, 98, 56, 83, 41], 
    [56, 92, 48, 37, 80], 
    [28, 46, 93, 54, 22], 
    [62, 99, 74, 50, 20], 
    [21, 84, 77, 96, 19], 
    [63, 29, 71, 48, 88], 
    [17, 11, 94, 22, 48], 
    [93, 66, 58, 54, 10], 
    [71, 96, 87, 35, 99], 
    [50, 82, 12, 73, 31], 
    [83, 64, 50, 72, 19], 
    [96, 53, 19, 60, 90], 
    [25, 68, 42, 55, 94], 
    [47, 81, 99, 72, 63], 
    [52, 35, 40, 91, 12], 
    [64, 58, 36, 22, 78], 
    [89, 46, 68, 94, 21]
])

a2 = np.array([63, 45, 76, 32, 14])

# Calculate distances for each row
for i, row in enumerate(a1):
    euclidean_distance = euclidean(row, a2)
    manhattan_distance = cityblock(row, a2)
    chebyshev_distance = chebyshev(row, a2)
    print(f"Distances for row {i}:")
    print("  Euclidean distance:", euclidean_distance)
    print("  Manhattan distance:", manhattan_distance)
    print("  Chebyshev distance:", chebyshev_distance)
