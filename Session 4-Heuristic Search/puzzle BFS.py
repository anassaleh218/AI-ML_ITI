# puzzle BFS
from queue import PriorityQueue


class PuzzleState:
    def __init__(self, board, parent=None, move=None, heuristic=0):
        self.board = board
        self.parent = parent
        self.move = move
        # self.depth = depth
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j
        return None


def misplaced_tiles(board, goal):
    sumofmissed = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                sumofmissed += 1
    return sumofmissed



def generate_neighbors(state, goal):
    neighbors = []
    empty_x, empty_y = state.find_empty()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_board = [row[:] for row in state.board]
            new_board[empty_x][empty_y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[empty_x][empty_y]
            heuristic = misplaced_tiles(new_board, goal)
            neighbors.append(PuzzleState(new_board, state, (new_x, new_y), heuristic))
    return neighbors


def greedy_best_first_search(start, goal):
    boardQueue = PriorityQueue()
    start_state = PuzzleState(start, heuristic=misplaced_tiles(start, goal))
    boardQueue.put(start_state)
    boardVisited = set()

    while not boardQueue.empty():
        current_state = boardQueue.get()

        if current_state.board == goal:
            return reconstruct_path(current_state)

        boardVisited.add(current_state)

        for neighbor in generate_neighbors(current_state, goal):
            if neighbor not in boardVisited:
                boardQueue.put(neighbor)

    return None


def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]


# Example usage
start = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

path = greedy_best_first_search(start, goal)
if path:
    for step in path:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")