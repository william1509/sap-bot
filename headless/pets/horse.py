from headless.context import Context
from headless.pets.pet import Pet
import random

class Horse(Pet):
    def __init__(self) -> None:
        super().__init__()
        self.AP = 2
        self.HP = 1
        self.tier = 1
        self.cost = 3
        self.name = 'Horse'

    def on_friend_summoned(friend, context: Context):
        friend.AP += 1