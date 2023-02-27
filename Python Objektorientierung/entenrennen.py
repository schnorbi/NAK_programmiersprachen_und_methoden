from abc import ABC, abstractmethod

class Duck(ABC):
    def __init__(self, typ):
        self.__distance = 0
        self.__typ = typ

    def run(self):
        self.__distance = self.__distance + self.distance_per_run()

    def get_distance(self):
        return self.__distance

    def get_typ(self):
        return self.__typ

    @abstractmethod
    def distance_per_run(self):
        pass

class TiringDuck(Duck):
    def __init__(self, factor, step_size):
        super().__init__('TiringDuck')
        self.__factor = factor
        self.__step_size = step_size

    def distance_per_run(self):
        local_step = self.__step_size
        self.__step_size = self.__step_size - self.__factor
        return local_step

class RandomDuck(Duck):
    def __init__(self, a, b):
        super().__init__('RandomDuck')
        self.__a = a
        self.__b = b

    def distance_per_run(self):
        import random
        return random.randint(self.__a, self.__b)

class DuckRace:
    def __init__(self):
        self.__ducks = []

    def add_duck(self, duck):
        self.__ducks.append(duck)

    def race(self):
        while True:
            for d in self.__ducks:
                d.run()
                if d.get_distance()>100:
                    return d

race = DuckRace()
race.add_duck(TiringDuck(0.5, 10))
race.add_duck(RandomDuck(5, 6))

winner = race.race()
print(winner.get_typ())