"""
Generic Genetic Algorithm.

See Classic Computer Science Problems in Python, Ch. 5
"""
from chromosome import Chromosome
from enum import Enum
from random import random, choices
from heapq import nlargest
from statistics import mean

class GeneticAlgorithm():
    SelectionType = Enum("SelectionType", "ROULETTE TOURNAMENT")

    def __init__(self, initial_population, threshold, max_generations=100,
                 mutation_chance=0.1, crossover_chance=0.7,
                 selection_type=SelectionType.TOURNAMENT):
        self._population = initial_population
        self._threshold = threshold
        self._max_generations = max_generations
        self._mutation_chance = mutation_chance
        self._crossover_chance = crossover_chance
        self._selection_type = selection_type
        self._fitness_key = type(initial_population[0]).fitness

    def _pick_roulette(self, wheel):
        """
        Given a 'roulette wheel' of probability weights, return a pair of 
        parents for propagation.

        The wheel is given by the individual fitness level of each 
        chromosome in a population relative to all other chromosomes in the
        population.
        """
        return tuple(choices(self._population, weights=wheel, k=2))

    def _pick_tournament(self, num_participants):
        """
        Returns the two chromosomes with the highest fitness level out of
        the randomly selected num_participants.
        """
        participants = choices(self._population, k=num_participants)
        return tuple(nlargest(2, participants, key=self._fitness_key))

    def _reproduce_and_replace(self):
        """
        Advance the population by one generation.

        New generation will have same size as previous generation.
        """
        new_population = []
        while len(new_population) < len(self._population):
            # Pick parents according to selection type
            if self._selection_type == GeneticAlgorithm.SelectionType.ROULETTE:
                parents = self._pick_roulette(
                    [x.fitness for x in self._population]
                )
            else:
                parents = self._pick_tournament(len(self._population) // 2)
            # Determine whether to crossover parents
            if random() < self._crossover_chance:
                new_population.extend(parents[0].crossover(parents[1]))
            else:
                new_population.extend(parents)
        # Due to the crossover, it is possible to have one more member of the
        # new population than there was in the original population.
        # Want to ensure that isn't the case
        if len(new_population) > len(self._population):
            new_population.pop()
        # Replace old generation
        self._population = new_population

    def _mutate(self):
        """
        Mutate individuals in the population according to mutation probability.
        """
        for individual in self._population:
            if random() < self._mutation_chance:
                individual.mutate()

    def run(self):
        best = max(self._population, key=self._fitness_key)
        for generation in range(self._max_generations):
            # Early termination if threshold is met
            if best.fitness() >= self._threshold:
                return best
            print("Generation {} | Best: {}".format(
                generation, best
            ))
            self._reproduce_and_replace()
            self._mutate()
            # See if new population has a better candidate
            highest = max(self._population, key=self._fitness_key)
            if highest.fitness() > best.fitness():
                best = highest
        return best
