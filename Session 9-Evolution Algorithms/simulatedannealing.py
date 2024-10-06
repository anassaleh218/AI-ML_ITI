import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class SimulatedAnnealingNQueens:
    def __init__(self, n, temp_start, temp_end, alpha, max_iter):
        self.n = n
        self.temp_start = temp_start
        self.temp_end = temp_end
        self.alpha = alpha
        self.max_iter = max_iter

        # Initialize state
        self.current_state = np.random.permutation(n) 
        self.current_attacks = self.calculate_attacks(self.current_state)
        self.best_state = self.current_state.copy()
        self.best_attacks = self.current_attacks
        self.temp = temp_start
        self.values = [self.current_attacks]

    def calculate_attacks(self, state):
        """Calculate the number of pairs of queens attacking each other."""
        attacks = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    attacks += 1
        return attacks

    def generate_neighbor(self, state):
        """Generate a neighbor state by swapping two queens."""
        neighbor = state.copy()
        idx1, idx2 = np.random.choice(self.n, 2, replace=False)
        neighbor[idx1], neighbor[idx2] = neighbor[idx2], neighbor[idx1]
        return neighbor

    def plot_board(self, state, title):
        """Plot the board state."""
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.n)
        ax.set_ylim(0, self.n)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(title)
        
        # Draw board
        for i in range(self.n):
            for j in range(self.n):
                color = 'white' if (i + j) % 2 == 0 else 'black'
                rect = patches.Rectangle((i, j), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
                ax.add_patch(rect)

        # Draw queens
        for i in range(self.n):
            ax.text(i + 0.5, state[i] + 0.5, 'Q', ha='center', va='center', fontsize=20, color='red')

        plt.gca().invert_yaxis()
        plt.show()

    def anneal(self):
        """Perform the simulated annealing algorithm."""
        for count in range(self.max_iter):
            # Generate a neighboring state
            neighbor = self.generate_neighbor(self.current_state)
            neighbor_attacks = self.calculate_attacks(neighbor)

            # Calculate the difference in the number of attacks
            delta = neighbor_attacks - self.current_attacks

            # Decide whether to accept the neighbor state
            if delta < 0 or np.random.rand() < np.exp(-delta / self.temp):
                self.current_state = neighbor
                self.current_attacks = neighbor_attacks
                if neighbor_attacks < self.best_attacks:
                    self.best_state = neighbor
                    self.best_attacks = neighbor_attacks

            # Update the temperature
            self.temp = max(self.temp * self.alpha, self.temp_end)
            self.values.append(self.best_attacks)

            # Print the current generation and attacks
            print(f"Generation {count}: Attacks {self.current_attacks}")

            # Plot the board every 100 iterations
            self.plot_board(self.current_state, f"Generation {count} - Attacks: {self.current_attacks}")

            # Stop if a solution with zero attacks is found
            if self.best_attacks == 0:
                print(f"Found solution with zero attacks at generation {count}")
                break

        return self.best_state, self.best_attacks, self.values

# Example usage
if __name__ == "__main__":
    # Parameters: size of board, initial temperature, final temperature, cooling rate, maximum iterations
    sa = SimulatedAnnealingNQueens(n=4, temp_start=1000, temp_end=0.1, alpha=0.95, max_iter=1000)
    best_state, best_attacks, values = sa.anneal()
    print("Best state (solution):", best_state)
    print("Number of attacks in the best state:", best_attacks)