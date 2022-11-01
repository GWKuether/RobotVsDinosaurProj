from weapon import Weapon



class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = [Weapon("Bazooka", 25), Weapon("Buzz Saw", 15), Weapon("Car Bomb", 40)]

    def attack(self, dinosaur):
        print(f"Using his {self.active_weapon[0].name}, {self.name} deals {self.active_weapon[0].attack_power} damage!")
        dinosaur.health -= self.active_weapon[0].attack_power

    def attack_2(self, dinosaur):
        print(f"Using his {self.active_weapon[1].name}, {self.name} deals {self.active_weapon[1].attack_power} damage!")
        dinosaur.health -= self.active_weapon[1].attack_power

    def attack_3(self, dinosaur):
        print(f"Using his {self.active_weapon[2].name}, {self.name} deals {self.active_weapon[2].attack_power} damage!")
        dinosaur.health -= self.active_weapon[2].attack_power