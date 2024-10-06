import random

class VacuumAgent:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)  # Starting position at (0, 0)

    def __str__(self) -> str:
        return f"the environment of vacuum agent is {self.environment}, {self.position}"

    def random_movement(self):
        # Randomly choose an action: move left, move right, move up, move down
        actions = ['left', 'right', 'up', 'down']
        action = random.choice(actions)
        if action == 'left' and self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])
        elif action == 'right' and self.position[0] < self.environment.width - 1:
            self.position = (self.position[0] + 1, self.position[1])
        elif action == 'up' and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif action == 'down' and self.position[1] < self.environment.height - 1:
            self.position = (self.position[0], self.position[1] + 1)
        # Clean if there's dirt
        self.clean_if_dirty()

    def systematic_movement(self):
        if self.position[1] % 2 == 0:  # Move right
            if self.position[0] < self.environment.width - 1:
                self.position = (self.position[0] + 1, self.position[1])
            else:
                self.position = (self.position[0], self.position[1] + 1)
        else:  # Move left
            if self.position[0] > 0:
                self.position = (self.position[0] - 1, self.position[1])
            else:
                self.position = (self.position[0], self.position[1] + 1)
        self.clean_if_dirty()

    def model_thinking_movement(self):
        possible_moves = {
            'left': (self.position[0] - 1, self.position[1]),
            'right': (self.position[0] + 1, self.position[1]),
            'up': (self.position[0], self.position[1] - 1),
            'down': (self.position[0], self.position[1] + 1)
        }

        for direction, pos in possible_moves.items():
            if 0 <= pos[0] < self.environment.width and 0 <= pos[1] < self.environment.height:
                if self.environment.is_dirty(pos):
                    self.position = pos
                    self.clean_if_dirty()
                    return  # Exit after cleaning

        self.random_movement()

    def clean_if_dirty(self):
        if self.environment.is_dirty(self.position):
            self.environment.clean(self.position)
            print(f"Agent cleaned dirt at position {self.position}")

    def run(self, steps=10):
        for _ in range(steps):
            print(f"Agent is at position {self.position}")
            self.model_thinking_movement()
            if not any(any(row) for row in self.environment.grid):
                print("All dirt is cleaned!")
                break

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[False for _ in range(height)] for _ in range(width)]  # Initialize grid with no dirt

    def add_dirt(self, position):
        self.grid[position[0]][position[1]] = True

    def clean(self, position):
        self.grid[position[0]][position[1]] = False

    def is_dirty(self, position):
        return self.grid[position[0]][position[1]]

    def print_grid(self):
        for row in self.grid:
            print(' '.join(['D' if cell else '.' for cell in row]))
        print()

env = Environment(width=5, height=5)
env.add_dirt((1, 1))
env.add_dirt((2, 3))

print("Grid after assigning the dirt:")
env.print_grid()

agent = VacuumAgent(environment=env)
agent.run(steps=10)

print("Final grid after cleaning:")
env.print_grid()

