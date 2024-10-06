import random

store_hours = 12

employees = [
    {"name": "Alice", "availability": list(range(0, 6)), "preferred": [1, 2], "skills": 5},
    {"name": "Bob", "availability": list(range(6, 12)), "preferred": [8, 9], "skills": 3},
    {"name": "Charlie", "availability": list(range(0, 12)), "preferred": [4, 5], "skills": 4},
    {"name": "Diana", "availability": list(range(3, 9)), "preferred": [6, 7], "skills": 2},
]

def fitness(schedule):
    score = 0
    
    for hour, employee_index in enumerate(schedule):
        employee = employees[employee_index]
        
        if hour not in employee["availability"]:
            score -= 5  
            
        if hour in employee["preferred"]:
            score += 3 
            
        score += employee["skills"]  
    
    return score

def generate_random_schedule():
    return [random.choice([i for i, emp in enumerate(employees) if hour in emp["availability"]]) for hour in range(store_hours)]

def crossover(parent1, parent2):
    split = random.randint(1, store_hours - 1)
    child1 = parent1[:split] + parent2[split:]
    child2 = parent2[:split] + parent1[split:]
    return child1, child2

def mutate(schedule):
    hour = random.randint(0, store_hours - 1)
    employee_index = random.choice([i for i, emp in enumerate(employees) if hour in emp["availability"]])
    schedule[hour] = employee_index

def genetic_algorithm(population_size=10, generations=100, mutation_rate=0.1):
    population = [generate_random_schedule() for _ in range(population_size)]
    
    for generation in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        
        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:population_size//2], 2)
            child1, child2 = crossover(parent1, parent2)
            next_generation += [child1, child2]
        
        for individual in next_generation:
            if random.random() < mutation_rate:
                mutate(individual)
        
        population = next_generation
    
    best_schedule = max(population, key=fitness)
    return best_schedule, fitness(best_schedule)

optimal_schedule, optimal_fitness = genetic_algorithm()

for hour, employee_index in enumerate(optimal_schedule):
    print(f"Hour {hour}: {employees[employee_index]['name']}")

print(f"Optimal fitness: {optimal_fitness}")
