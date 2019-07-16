"""
Module specifying a base Chromosome class that is capable of various methods
needed for genetic algorithms.

See Classic Computer Science Problems in Python Ch. 5.1
"""
from abc import ABC, abstractmethod

class Chromosome(ABC):
    """
    Generic base class for units in genetic algorithms.
    """
    @abstractmethod
    def fitness(self):
        pass

    @classmethod
    @abstractmethod
    def random_instance(cls):
        pass

    @abstractmethod
    def crossover(self, other):
        pass

    @abstractmethod
    def mutate(self):
        pass
