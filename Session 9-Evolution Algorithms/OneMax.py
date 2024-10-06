import random

def onemax_fitness(bitstring):
    return sum(bitstring)

def random_bitstring(length):
    return [random.randint(0, 1) for _ in range(length)]

def mutate(bitstring):
    mutant = bitstring[:]
    index = random.randint(0, len(bitstring) - 1)
    mutant[index] = 1 if mutant[index] == 0 else 0
    return mutant

def hill_climbing(bitstring, max_iter):
    current = bitstring
    current_fitness = onemax_fitness(current)
    
    for iteration in range(max_iter):
        neighbor = mutate(current)
        neighbor_fitness = onemax_fitness(neighbor)
        
        if neighbor_fitness > current_fitness:
            current, current_fitness = neighbor, neighbor_fitness
            print(f"Iteration {iteration}: Better solution found with fitness {current_fitness}")
        
        if current_fitness == len(bitstring):
            break
    
    return current, current_fitness

bitstring_length = 20
max_iterations = 1000

initial_bitstring = random_bitstring(bitstring_length)

solution, fitness = hill_climbing(initial_bitstring, max_iterations)

print("\nFinal solution:", solution)
print("Final fitness:", fitness)
