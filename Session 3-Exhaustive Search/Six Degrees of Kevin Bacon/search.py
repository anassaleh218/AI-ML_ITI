import csv
import sys

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}

directory = "D:\\Studying\\Courses\\ITI-Summer Code Camp\\AI & ML\\Anas Saleh Mousa\\Session 3\\"  # Replace with your actual directory path

class Node:
    def __init__(self, state, parent, action):
        self.state = state  # Person ID
        self.parent = parent  # Parent Node
        self.action = action  # Movie ID

    def __repr__(self):
        return f"Node(state={self.state}, action={self.action})"


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            return self.frontier.pop()

class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            return self.frontier.pop(0)

def load_data():
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass

def main():
    # Load data from files into memory
    print("Loading data...")
    load_data()
    print("Data loaded.")

    # Print results
    print("Names Dictionary:")
    print(names)
    print("\nPeople Dictionary:")
    print(people)
    print("\nMovies Dictionary:")
    print(movies)
    #


    source_name = input("Name: ").strip().lower()
    target_name = input("Name: ").strip().lower()

    source = person_id_for_name(source_name)
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(target_name)
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        path = [(None, source)] + path
        # print(path) #Print Path
        for i in range(len(path) - 1):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):

    solution_found = False
    no_solution = False
    solution = []

    initial = Node(state=source, parent=None, action=None)
    frontier = StackFrontier() #Choose
    frontier.add(initial)
    explored = set()
    while not solution_found:

        if frontier.empty():
            no_solution = True
            solution_found = True

        node = frontier.remove()

        if node.state == target:
            # Return the solution
            solution_found = True
            while node.parent is not None:
                pid, mid = node.state, node.action
                solution.append((mid, pid))
                node = node.parent
            solution.reverse()

        explored.add(node.state)

        children = neighbors_for_person(node.state)
        for movie_id, neighbor in children:
            if not frontier.contains_state(neighbor) and neighbor not in explored:
                child_node = Node(state=neighbor, action=movie_id, parent=node)
                frontier.add(child_node)
                if child_node.state == target:
                    # Return the solution
                    solution_found = True
                    while child_node.parent is not None:
                        pid, mid = child_node.state, child_node.action
                        solution.append((mid, pid))
                        child_node = child_node.parent
                    solution.reverse()

    if solution_found:
        if no_solution:
            return None
        return solution

def person_id_for_name(name):

    person_ids = names.get(name.lower(), set())

    if len(person_ids) == 0:
        return None

    if len(person_ids) == 1:
        return list(person_ids)[0]

    return None


def neighbors_for_person(person_id):
    # """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for neighbor_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, neighbor_id))
    return neighbors

if __name__ == "__main__":

    main()
