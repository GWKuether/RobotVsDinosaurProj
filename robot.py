from weapon import Weapon



class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Bazooka", 25)

    def attack(self, dinosaur):
        print(f"using his {self.active_weapon.name}, {self.name} deals {self.active_weapon.attack_power} damage!")
        dinosaur.health -= self.active_weapon.attack_power