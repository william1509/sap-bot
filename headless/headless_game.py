from typing import List

from headless.invalid_action_exception import InvalidActionException
from headless.context import Context

from headless.pets.pet import Pet
import headless.constants as constants
import random
import math

class HeadlessGame:

    squad: List[Pet]
    shop: List[Pet]
    current_tier: int
    gold: int

    context: Context

    automatic: bool

    def __init__(self, automatic=False) -> None:
        self.squad = [None for _ in range(0, 5)]
        self.shop = []
        self.current_tier = 1
        self.automatic = automatic
        self.gold = 10
        self.context = Context(self.gold, self.squad, self.shop)
        

    def refresh_shop(self):
        # Instantiating the pets
        self.shop = [x() for x in self.get_random_pets()]

    def get_random_pets(self):
        self.shop.clear()
        return random.choices(constants.playable_pets[self.current_tier], k=constants.n_shop_slots_per_tier[self.current_tier])

    def play(self):
        game_over = False
        while not game_over:
            # New turn starts
            self.refresh_shop()
            self.gold =  10
            turn_over = False
            while not turn_over:
                print('Shop:\n%s\nSquad:\n%s\n' % (self.shop, self.squad))
                turn_over = self.execute_command()
                pass

    def summon(self, pet: Pet):
        self.squad.append(pet)

        # on_bought
        pet.on_bought(self.context)
        pet.on_summoned(self.context)

        # on_friend_bought
        others = self.context.other_pets(pet)
        for p in others:
            p.on_friend_bought(self.context)

    """
    Action must be formatted like the following:
        b 1 2: Buys the first pet in the shop and places it on the second spot in the squad
        bc 1 2: Buys the first pet in the shop and combines it with the second pet in the squad
        s 1: Sells the first pet of the squad
        c 1 2: Combines the first and second squad pets by placing the first pet on the second pet
        m 3 1: Moves the third pet to the first spot
        e: Ends the turn
        r: Roll

        Returns False if the turns is over, True if it's not
    """
    def execute_command(self):
        if self.automatic:
            pass
        else:
            command = input("Enter action :")
            try:
                tokens = command.lower().split(' ')
                action = tokens[0]
                val_1 = tokens[1]
                
                if not action == 's':
                    val_2 = tokens[2]

                if action == 'e':
                    return True
                
                match action:
                    case 'b':
                        print(f'Buying {self.shop[int(val_1)]}')
                        self.buy(int(val_1), int(val_2))
                        print(self.squad)
                    case 'bc':
                        print(f'Buying and combine {self.shop[int(val_1)]}')
                        print(self.squad)
                    case 's':
                        print(f'Selling {self.shop[int(val_1)]}')
                        print(self.squad)
                    case 'c':
                        print(f'Combine {self.squad[int(val_1)]}')
                        self.combine(int(val_1), int(val_2))
                        print(self.squad)
                    case 'm':
                        print(f'Move {self.shop[int(val_1)]}')
                        print(self.squad)
                    case 'r':
                        self.refresh_shop()
                    case other:
                        raise(f'{other} is an invalid action')

            except IndexError:
                raise('Command not formatted correctly')

            return False
    
    def combine(self, pos1: int, pos2: int):

        if pos1 > len(self.squad):
            raise InvalidActionException(f"There is no pet {pos1} in your squad")

        if pos2 > len(self.squad):
            raise InvalidActionException(f"There is no pet {pos2} in your squad")

        pet1 = self.squad[pos1]
        pet2 = self.squad[pos2]

        hp = max(pet1.HP, pet2.HP) + 1
        ap = max(pet1.AP, pet2.AP) + 1
        xp = pet1.XP + pet2.XP
        
        if xp >= 6:
            raise InvalidActionException('XP bigger than 6')

        bigger_pet, smaller_pet = pet1, pet2 if pet1.XP >= pet2.XP else pet2, pet1

        if self.is_level_up(bigger_pet.XP, smaller_pet.XP):
            # on_level_up
            bigger_pet.on_level_up(self.context)

            # on_friend_level_up
            others = self.context.other_pets(bigger_pet)
            for p in others:
                p.on_friend_level_up(self.context)

        bigger_pet.XP += smaller_pet.XP
        bigger_pet.AP = math.floor(ap, 50)
        bigger_pet.HP = math.floor(hp, 50)

    def is_level_up(current_xp: int, xp: int) -> bool:
        return (current_xp <= 2 and xp >= 2) or (current_xp > 2 and xp == 3)

    def buy(self, shop_pos: int, squad_pos: int):
        if shop_pos > len(self.shop):
            raise InvalidActionException(f"There is no pet {shop_pos} in the shop")
        
        n_pet_in_squad = [x for x in self.squad if x is not None]
        if len(n_pet_in_squad) == constants.squad_max_size:
            raise InvalidActionException(f"Squad is already full")

        # move pets to insert the new one
        if self.squad[squad_pos] is None:
            pet = self.shop[shop_pos]
            self.squad[squad_pos] = pet
        else: 
            empty_spot = None
            for i in range(squad_pos, -1, -1):
                if self.squad[i] is None:
                    empty_spot = i
                    break
            
            if empty_spot is None:
                for i in range(squad_pos, constants.squad_max_size):
                    if self.squad[i] is None:
                        empty_spot = i
                        break
                                
            # If adjacent, we simply swap
            # This code sucks
            diff = abs(empty_spot - squad_pos)
            if diff == 1:
                self.squad[empty_spot], self.squad[squad_pos] = self.squad[squad_pos], self.squad[empty_spot]

                pet = self.shop[shop_pos]
                self.squad[squad_pos] = pet
            elif diff == 2:
                iterator = -1 if empty_spot > squad_pos else 1

                self.squad[empty_spot], self.squad[empty_spot + iterator] = self.squad[empty_spot + iterator], self.squad[empty_spot]
                self.squad[empty_spot + iterator], self.squad[empty_spot + iterator * 2] = self.squad[empty_spot + iterator * 2], self.squad[empty_spot + iterator]
                
                pet = self.shop[shop_pos]
                self.squad[squad_pos] = pet

            



            
