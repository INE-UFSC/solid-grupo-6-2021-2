"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""

from abc import abstractmethod


class StatsReporter:
    def __init__(self):
        pass

    @abstractmethod
    def report(self):
        pass


class Player(StatsReporter):
    def __init__(self, name):
        super(Player, self).__init__()
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
