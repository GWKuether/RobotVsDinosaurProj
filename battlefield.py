from dinosaur import Dinosaur
from robot import Robot



class Battlefield():
    def __init__(self):
        self.dinosaur_fighter = Dinosaur("Large Jenny", 25)
        self.robot_fighter = Robot("Aluminum Cowboy")
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print(f"Welcome to the death match of the century.\n{self.dinosaur_fighter.name} Vs. {self.robot_fighter.name}\nWho will survive?")

    def battle_phase(self):
        self.dinosaur_fighter.attack(self.robot_fighter)
        print(f"{self.robot_fighter.name} has {self.robot_fighter.health} health left!")
        self.robot_fighter.attack(self.dinosaur_fighter)
        print(f"{self.dinosaur_fighter.name} has {self.dinosaur_fighter.health} health left!")

    def display_winner(self):
        pass