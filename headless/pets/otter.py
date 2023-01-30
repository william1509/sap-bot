from headless.context import Context
from headless.pets.pet import Pet
import random

class Otter(Pet):
    def __init__(self) -> None:
        super().__init__()
        self.AP = 1
        self.HP = 2
        self.tier = 1
        self.cost = 3
        self.name = 'Otter'

    def on_bought(self, context: Context):
        pet = random.choice(context.other_pets(self))
        pet.AP += 1
        pet.HP += 1