# 1.	Using Genetic Algorithm  for solving N-Queen problem
import random

def fitness(chromosome):
    n = len(chromosome)
    conflicts = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == j - i:
                conflicts += 1
                
    return n * (n - 1) // 2 - conflicts  

def selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    selected = random.choices(population, probabilities, k=len(population))
    return selected

def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 2)
    child = parent1[:point] + [gene for gene in parent2 if gene not in parent1[:point]]
    return child

def mutate(chromosome, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

def genetic_algorithm(n, population_size=100, generations=1000):
    population = [random.sample(range(n), n) for _ in range(population_size)]
    
    for generation in range(generations):
        fitnesses = [fitness(chromosome) for chromosome in population]
    
        if max(fitnesses) == n * (n - 1) // 2:
            break
        
        selected_population = selection(population, fitnesses)
        population = [mutate(crossover(random.choice(selected_population), random.choice(selected_population)))
                      for _ in range(population_size)]
    
    best_chromosome = max(population, key=fitness)
    return best_chromosome, fitness(best_chromosome)

n = 8
solution, solution_fitness = genetic_algorithm(n)
print(f"Solution: {solution}, Fitness: {solution_fitness}")
