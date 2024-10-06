import os
import cv2
import numpy as np
import pandas as pd
from skimage.filters import prewitt_h, prewitt_v, threshold_minimum

def extract_edge_features(image):
    edges_prewitt_horizontal = prewitt_h(image)
    edges_prewitt_vertical = prewitt_v(image)
    return np.concatenate([edges_prewitt_horizontal.ravel(), edges_prewitt_vertical.ravel()])

def extract_histogram_features(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist.flatten()

def extract_thresholding_features(image):
    thresh_min = threshold_minimum(image)
    binary_min = image > thresh_min
    return binary_min.ravel()

def process_images(yes_directory, no_directory, output_csv):
    # Initialize lists to hold features and labels
    features_list = []
    labels_list = []

    # Function to process a directory
    def process_directory(directory, label):
        for filename in os.listdir(directory):
            if filename.endswith(('.jpg', '.png', '.jpeg')):  # Add more extensions if needed
                image_path = os.path.join(directory, filename)
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                
                # Extract features
                # edge_features = extract_edge_features(image)
                # hist_features = extract_histogram_features(image)
                thresholding_features = extract_thresholding_features(image)
                
                # Combine all features
                # features = np.concatenate([edge_features, hist_features, thresholding_features])

                # seperate feature
                features = thresholding_features
                
                # Append to lists
                features_list.append(features)
                labels_list.append(label)

    # Process 'yes' images
    process_directory(yes_directory, 'yes')
    
    # Process 'no' images
    process_directory(no_directory, 'no')

    # Convert lists to DataFrame
    df = pd.DataFrame(features_list)
    df['label'] = labels_list

    # Save DataFrame to CSV
    df.to_csv(output_csv, index=False)

    print(f"Features saved to {output_csv}")

# Example usage
# process_images('brain_tumor_dataset/yes', 'brain_tumor_dataset/no', 'edge_features.csv')
# process_images('brain_tumor_dataset/yes', 'brain_tumor_dataset/no', 'hist_features.csv')
process_images('brain_tumor_dataset/yes', 'brain_tumor_dataset/no', 'thresholding_features.csv')
