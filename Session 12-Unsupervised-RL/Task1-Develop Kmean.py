# Task1 Develop Kmean and don't use Build in functions or library
import pandas as pd
import random
import math
import matplotlib.pyplot as plt


def euclidean_distance(point1, point2):
    return math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2))

# Initialize centroids randomly from the dataset
def initialize_centroids(data, k):
    centroids = random.sample(data, k)
    return centroids


# Assign each point to the nearest centroid
def assign_clusters(data, centroids):
    clusters = [[] for _ in range(len(centroids))]
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        min_distance_index = distances.index(min(distances))
        clusters[min_distance_index].append(point)
    return clusters

# Update centroids
def update_centroids(clusters):
    new_centroids = []
    for cluster in clusters:
        if len(cluster) == 0:
            continue  # Avoid division by zero
        avg_lat = sum([point[0] for point in cluster]) / len(cluster)
        avg_long = sum([point[1] for point in cluster]) / len(cluster)
        new_centroids.append((avg_lat, avg_long))
    return new_centroids

# Calculate WCSS for a given clustering
def calculate_wcss(clusters, centroids):
    wcss = 0
    for i, cluster in enumerate(clusters):
        for point in cluster:
            # sum of square
            wcss += euclidean_distance(point, centroids[i]) ** 2
    return wcss

# K-means algorithm
def kmeans(data, k, max_iterations=100):
    # random
    centroids = initialize_centroids(data, k)
    
    for i in range(max_iterations):
        ##### assign_clusters: make clusters by assign data to nearest centroid 
        clusters = assign_clusters(data, centroids)
        # through avg
        new_centroids = update_centroids(clusters)
        
        # Check convergence
        if new_centroids == centroids:
            break
        
        centroids = new_centroids
    
    wcss = calculate_wcss(clusters, centroids)
    return centroids, clusters, wcss


def plot_kmeans_results(k, centroids, wcss, data):
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'gray']
    
    # Assign clusters based on the current centroids
    clusters = assign_clusters(data, centroids)

    plt.figure(figsize=(10, 6))
    
    # Plot clusters
    for i, cluster in enumerate(clusters):
        if len(cluster) == 0:
            continue
        cluster_points = zip(*cluster)
        plt.scatter(*cluster_points, color=colors[i % len(colors)], label=f'Cluster {i+1}')
    
    # Plot centroids
    centroid_points = zip(*centroids)
    plt.scatter(*centroid_points, color='black', marker='x', s=100, label='Centroids')
    
    # Adding labels and title
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title(f'K-means Clustering (K={k}), WCSS={wcss:.2f}')
    plt.legend()
    plt.grid(True)
    
    # Show plot
    plt.show()

# Load data
dataset = pd.read_csv('Countryclusters.csv')
lat = pd.DataFrame(dataset.iloc[:, 1])
long = pd.DataFrame(dataset.iloc[:, 2])
data = list(zip(lat['latitude'], long['longitude']))

results = []

# Run K-means for different k values and plot results
k_values = range(1, 7)  # For k values from 1 to 6

for k in k_values:
    centroids, clusters, wcss = kmeans(data, k)
    results.append((k, centroids, clusters, wcss))
    print(f"K={k}, WCSS={wcss}, Centroids={centroids}")
    
# print(results)
centroids==[(15.675507523809523, 56.89712961904762), (-4.954837880952381, 8.792527452380952), (-15.7990057, -164.167216), (9.8465647, -70.34407094), (46.03195261904762, 12.814663031746031), (7.59836127027027, 130.71677983783783)]
plot_kmeans_results(6, centroids, 161941.52793568888, data)   
  
