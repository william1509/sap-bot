from headless.pets.fish import Fish
from headless.pets.horse import Horse
from headless.pets.otter import Otter


n_shop_slots_per_tier = {
    1: 3,
    2: 3,
    3: 4,
    4: 4,
    5: 5,
    6: 5
}

playable_pets = {
    1: [
        Fish,
        Otter,
        Horse
    ]
}

squad_max_size = 5