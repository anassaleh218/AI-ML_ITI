import tkinter as tk
from tkinter import filedialog
from queue import Queue, LifoQueue, PriorityQueue

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class MazeSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver")
        self.root.geometry("480x700")  

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack(padx=10, pady=10)

        self.maze = []
        self.start = None
        self.end = None
        self.current_path = None  

        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="x", padx=10)

        self.create_styled_button(button_frame, "Load Maze", self.load_maze)
        self.create_styled_button(button_frame, "Solve with BFS", lambda: self.solve_maze(self.bfs))
        self.create_styled_button(button_frame, "Solve with DFS", lambda: self.solve_maze(self.dfs))
        self.create_styled_button(button_frame, "Solve with A* (Heuristic)", lambda: self.solve_maze(self.a_star))

    def create_styled_button(self, frame, text, command):
        """ Helper method to create styled buttons """
        button = tk.Button(
            frame,
            text=text,
            command=command,
            bg="#4CAF50",  # Background color (green)
            fg="white",  # Text color
            font=("Helvetica", 14),  # Font and size
            height=2,  # Button height (in lines)
            bd=0,  # Remove button border
            activebackground="#45a049",  # Button background color when clicked
            activeforeground="white"  # Text color when clicked
        )
        button.pack(fill="x", pady=5) 

    def load_maze(self):
        file_path = filedialog.askopenfilename()
        with open(file_path, "r") as file:
            self.maze = [list(line.strip()) for line in file.readlines()]
        
        for r, row in enumerate(self.maze):
            for c, cell in enumerate(row):
                if cell == 'A':
                    self.start = (r, c)
                elif cell == 'B':
                    self.end = (r, c)

        self.current_path = None  

        self.draw_maze()

    def draw_maze(self):
        self.canvas.delete("all")
        rows, cols = len(self.maze), len(self.maze[0])
        cell_width = self.canvas.winfo_width() // cols
        cell_height = self.canvas.winfo_height() // rows
        
        for r in range(rows):
            for c in range(cols):
                x1, y1 = c * cell_width, r * cell_height
                x2, y2 = x1 + cell_width, y1 + cell_height
                color = "white"
                if self.maze[r][c] == '#':
                    color = "black"
                elif self.maze[r][c] == 'A':
                    color = "green"
                elif self.maze[r][c] == 'B':
                    color = "red"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_path(self, path):
        if self.current_path:
            self.clear_path(self.current_path)
        
        self.current_path = path 
        rows, cols = len(self.maze), len(self.maze[0])
        cell_width = self.canvas.winfo_width() // cols
        cell_height = self.canvas.winfo_height() // rows
        
        # Draw the path
        for r, c in path:
            x1, y1 = c * cell_width, r * cell_height
            x2, y2 = x1 + cell_width, y1 + cell_height
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")

        # Redraw the start and end points to maintain their colors
        if self.start:
            sr, sc = self.start
            x1, y1 = sc * cell_width, sr * cell_height
            x2, y2 = x1 + cell_width, y1 + cell_height
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

        if self.end:
            er, ec = self.end
            x1, y1 = ec * cell_width, er * cell_height
            x2, y2 = x1 + cell_width, y1 + cell_height
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")

    def clear_path(self, path):
        rows, cols = len(self.maze), len(self.maze[0])
        cell_width = self.canvas.winfo_width() // cols
        cell_height = self.canvas.winfo_height() // rows

        for r, c in path:
            x1, y1 = c * cell_width, r * cell_height
            x2, y2 = x1 + cell_width, y1 + cell_height
            color = "white"
            if self.maze[r][c] == '#':
                color = "black"
            elif self.maze[r][c] == 'A':
                color = "green"
            elif self.maze[r][c] == 'B':
                color = "red"
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def solve_maze(self, algorithm):
        if not self.start or not self.end:
            return
        path = algorithm(self.start, self.end)
        if path:
            self.draw_path(path)

    def bfs(self, start, end):
        queue = Queue()
        queue.put((start, [start]))
        visited = set()

        while not queue.empty():
            (r, c), path = queue.get()
            if (r, c) == end:
                return path
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if self.is_valid(nr, nc, visited):
                    queue.put(((nr, nc), path + [(nr, nc)]))
        return None

    def dfs(self, start, end):
        stack = LifoQueue()
        stack.put((start, [start]))
        visited = set()

        while not stack.empty():
            (r, c), path = stack.get()
            if (r, c) == end:
                return path
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if self.is_valid(nr, nc, visited):
                    stack.put(((nr, nc), path + [(nr, nc)]))
        return None

    def a_star(self, start, end):
        def heuristic(pos):
            return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

        pq = PriorityQueue()
        pq.put((0, start, [start]))
        visited = set()

        while not pq.empty():
            _, (r, c), path = pq.get()
            if (r, c) == end:
                return path
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if self.is_valid(nr, nc, visited):
                    pq.put((heuristic((nr, nc)), (nr, nc), path + [(nr, nc)]))
        return None

    def is_valid(self, r, c, visited):
        return (0 <= r < len(self.maze) and 0 <= c < len(self.maze[0]) and
                self.maze[r][c] != '#' and (r, c) not in visited)

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeSolverGUI(root)
    root.mainloop()
