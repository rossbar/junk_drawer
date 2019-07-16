"""
Naive test of genetic algorithm for finding maximum of simple equation with
analytic solution (for testing).

See Classic Computer Science Problems in Python, Ch. 5.3
"""
from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm
from random import random, randrange
from copy import deepcopy

class SimpleEquation(Chromosome):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fitness(self):
        """
        Solve 6x - x**2 + 4y - y**2
        """
        return 6 * self.x - self.x**2 + 4 * self.y - self.y**2

    @classmethod
    def random_instance(cls):
        return SimpleEquation(randrange(100), randrange(100))

    def crossover(self, other):
        child1 = deepcopy(self)
        child2 = deepcopy(other)
        child1.y = other.y
        child2.y = self.y
        return child1, child2

    def mutate(self):
        if random() > 0.5:  # Mutate x
            if random() > 0.5:
                self.x += 1
            else:
                self.x -= 1
        else:
            if random() > 0.5:
                self.y += 1
            else:
                self.y -= 1

    def __str__(self):
        return "x = {} | y = {} | fitness = {}".format(
            self.x, self.y, self.fitness()
        )

if __name__ == "__main__":
    initial_population = [SimpleEquation.random_instance() for _ in range(20)]
    ga = GeneticAlgorithm(initial_population, threshold=13,
                          max_generations=100, mutation_chance=0.1, 
                          crossover_chance=0.7)
    result = ga.run()
    print(result)

