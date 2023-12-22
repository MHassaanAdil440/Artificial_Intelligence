import random

def generate_individual(length):
    """Generate a random binary string."""
    return ''.join(random.choice('01') for _ in range(length))

def calculate_fitness(individual, target):
    """Calculate the fitness of an individual based on its similarity to the target."""
    return sum(1 for a, b in zip(individual, target) if a == b)

def crossover(parent1, parent2):
    """Perform crossover (single-point crossover in this example)."""
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mutation_rate):
    """Perform mutation."""
    mutated = ''.join(
        bit if random.random() > mutation_rate else random.choice('01')
        for bit in individual
    )
    return mutated

def genetic_algorithm(target, population_size, mutation_rate, generations):
    """Genetic algorithm to evolve a population to match the target."""
    population = [generate_individual(len(target)) for _ in range(population_size)]

    for generation in range(generations):
        # Evaluate fitness
        fitness_scores = [calculate_fitness(individual, target) for individual in population]

        # Select parents based on fitness
        parents = [population[i] for i in range(population_size) if random.random() < fitness_scores[i] / len(target)]

        # Crossover and mutate to create new generation
        new_population = []
        while len(new_population) < population_size:
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

        # Check for success
        best_individual = max(population, key=lambda x: calculate_fitness(x, target))
        if calculate_fitness(best_individual, target) == len(target):
            print(f"Target achieved in generation {generation + 1}! Best individual: {best_individual}")
            break

if __name__ == "__main__":
    target_string = "1101101010101010111000001111"
    population_size = 100
    mutation_rate = 0.01
    generations = 1000

    genetic_algorithm(target_string, population_size, mutation_rate, generations)
