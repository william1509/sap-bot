from headless.context import Context
from headless.pets.pet import Pet


class Fish(Pet):
    def __init__(self) -> None:
        super().__init__()
        self.AP = 2
        self.HP = 2
        self.tier = 1
        self.cost = 3
        self.name = 'Fish'

    def on_level_up(context: Context):
        for pet in context.squad:
            pet.AP += 1
            pet.HP += 1
    