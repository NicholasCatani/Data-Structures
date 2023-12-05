### Simulation of an ecosystem

import random

class Animal:
    def __init__(self, species):
        self.species = species

class Bear(Animal):
    pass

class Fish(Animal):
    pass

def initialize_ecosystem(size, initial_bears, initial_fish):
    ecosystem = [None] * size

    for _ in range(initial_bears):
        index = random.randint(0, size - 1)
        while ecosystem[index] is not None:
            index = random.randint(0, size - 1)
        ecosystem[index] = Bear("Bear")

    for _ in range(initial_fish):
        index = random.randint(0, size - 1)
        while ecosystem[index] is not None:
            index = random.randint(0, size - 1)
        ecosystem[index] = Fish("Fish")

    return ecosystem

def display_ecosystem(ecosystem):
    for animal in ecosystem:
        if animal is None:
            print("None", end=" ")
        else:
            print(animal.species, end=" ")
    print()

def simulate_ecosystem(ecosystem, num_steps):
    size = len(ecosystem)

    for _ in range(num_steps):
        for i in range(size):
            if ecosystem[i] is not None:
                move_to = random.choice([i-1, i, i+1]) % size     # Move to the left, stay, or to the right
                if ecosystem[move_to] is None:
                    ecosystem[move_to] = ecosystem[i]
                    ecosystem[i] = None
                else:
                    if type(ecosystem[i]) == type(ecosystem[move_to]):
                        new_index = random.choice([i for i in range(size) if ecosystem[i] is None])
                        ecosystem[new_index] = type(ecosystem[i])()
                    elif (isinstance(ecosystem[i], Bear) and isinstance(ecosystem[move_to], Fish)) or \
                            (isinstance(ecosystem[i], Fish) and isinstance(ecosystem[move_to], Bear)):
                        ecosystem[move_to] = None

        display_ecosystem(ecosystem)
        print()

if __name__ == "__main__":
    river_size = 10
    initial_bears = 3
    initial_fish = 12
    simulation_steps = 5

    river_ecosystem = initialize_ecosystem(river_size, initial_bears, initial_fish)
    print("Initial Ecosystem:")
    display_ecosystem(river_ecosystem)
    print()

    print("Simulation Steps:")
    simulate_ecosystem(river_ecosystem, simulation_steps)

