from dataclasses import dataclass
from typing import List


@dataclass
class Context:
    gold: int
    squad: List
    shop: List

    def other_pets(self, pet):
        return list(filter(lambda x: x != pet, self.squad))