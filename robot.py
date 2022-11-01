from weapon import Weapon



class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Bazooka", 25)
        self.active_weapon_2 = Weapon("Buzz Saw", 15)
        self.active_weapon_3 = Weapon("Car Bomb", 40)

    def attack(self, dinosaur):
        print(f"Using his {self.active_weapon.name}, {self.name} deals {self.active_weapon.attack_power} damage!")
        dinosaur.health -= self.active_weapon.attack_power

    def attack_2(self, dinosaur):
        print(f"Using his {self.active_weapon_2.name}, {self.name} deals {self.active_weapon_2.attack_power} damage!")
        dinosaur.health -= self.active_weapon_2.attack_power

    def attack_3(self, dinosaur):
        print(f"Using his {self.active_weapon_3.name}, {self.name} deals {self.active_weapon_3.attack_power} damage!")
        dinosaur.health -= self.active_weapon_3.attack_power