# 2.	Using GA for solving TSP problem
import random
import math

# Number of cities
NUM_CITIES = 10

# Population size
POPULATION_SIZE = 100

CITIES = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(NUM_CITIES)] #[(23, 45), (67, 89), (12, 34), (56, 78), (90, 10)]

class Individual(object):
    '''
    Class representing individual in population
    '''

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()
        
    @classmethod #static Method
    def  create_gnome(self):
        '''
        create random genes for mutation
        '''
        gnome = random.sample(range(NUM_CITIES),NUM_CITIES) #[2,3,8,9,..]
        return gnome
    
    def mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''

        child_chromosome = [-1]*NUM_CITIES #[-1,..]
        
        start, end = sorted(random.sample(range(NUM_CITIES), 2)) #self
        child_chromosome[start:end] = self.chromosome[start:end] #child_chromosome=[-1..[start:end]..-1]
        
        pointer = 0
        for gene in par2.chromosome:
            if gene not in child_chromosome:
                while child_chromosome[pointer] != -1:
                    pointer += 1
                child_chromosome[pointer] = gene



        if random.random() < 0.1:
            swap_idx = random.sample(range(NUM_CITIES), 2)
            child_chromosome[swap_idx[0]], child_chromosome[swap_idx[1]] = child_chromosome[swap_idx[1]], child_chromosome[swap_idx[0]]

        return Individual(child_chromosome)

        
    def cal_fitness(self):
        '''
        Calculate fittness score, it is the number of
        characters in string which differ from target
        string.
        '''
        total_distance = 0
        for i in range(NUM_CITIES):
            city1 = CITIES[self.chromosome[i]]
            city2 = CITIES[self.chromosome[(i + 1) % NUM_CITIES]]
            total_distance += math.dist(city1, city2)
        return total_distance

def main():
    MAX_GENERATIONS=10
    generation = 1
    found = False
    population = []

    # Create initial population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))

    while not found and generation < MAX_GENERATIONS:
        # Sort population by fitness (lower is better for TSP)
        population = sorted(population, key=lambda x: x.fitness)

        # Print the best route in the current generation
        print(f"Generation: {generation}\tBest Route: {population[0].chromosome}\tDistance: {population[0].fitness}")

        # If the optimal solution is found (distance below a certain threshold)
        if population[0].fitness <= 0:
            found = True
            break

        # Create new generation
        new_generation = []

        # Elitism: Carry forward a few of the best routes unchanged
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        # Generate offspring
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation

        generation += 1

    print(f"Optimal route found in Generation {generation} with Distance: {population[0].fitness}")
    print(f"Route: {population[0].chromosome}")

if __name__ == '__main__':
    main()