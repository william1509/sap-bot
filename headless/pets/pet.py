from dataclasses import dataclass

from headless.context import Context

class Pet:

    name: str
    HP: int
    AP: int
    tier: int
    cost: int
    XP: int

    def __init__(self) -> None:
        self.XP = 0


    def on_level_up(context: Context):
        pass
    def on_friend_level_up(context: Context):
        pass
    def on_friend_bought(context: Context):
        pass
    def on_friend_sold(context: Context):
        pass
    def on_bought(context: Context):
        pass
    def on_sold(context: Context):
        pass
    def on_faint(context: Context):
        pass
    def on_friend_faint(context: Context):
        pass
    def on_summoned(context: Context):
        pass
    def on_friend_summoned(friend, context: Context):
        pass
    def on_start_of_battle(context: Context):
        pass
    def on_start_of_turn(context: Context):
        pass
    def __str__(self):
        return f'{self.HP} hp {self.AP} ap {self.XP} xp'
    def __repr__(self):
        return f'{self.name}<{self.HP} hp {self.AP} ap {self.XP} xp>'