# Task 0
import numpy as np
import matplotlib.pyplot as plt


def temperature_distribution(K, L, G, Tw, grid_size=50):
    # Define the grid
    x_vals = np.linspace(0, 3, grid_size)
    y_vals = np.linspace(0, 3, grid_size)
    x, y = np.meshgrid(x_vals, y_vals)

    # Calculate the temperature using the provided formula
    temp = ((G * L) / (2 * K)) * (1 - x / L) + Tw

    return x, y, temp


def MeshGridEXM():
    K = 50  # Thermal conductivity
    L = 0.5  # Thickness of the wall
    G = 100  # Heat generation rate
    Tw = 300  # Surface temperature

    x, y, T = temperature_distribution(K, L, G, Tw)

    # Plot the temperature distribution
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, T, cmap='hot')

    # Set labels for the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Temperature')
    ax.set_title('Temperature Distribution Across the Wall')
    plt.show()


MeshGridEXM()
