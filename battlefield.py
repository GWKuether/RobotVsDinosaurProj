from dinosaur import Dinosaur
from robot import Robot



class Battlefield():
    def __init__(self):
        self.dinosaur = Dinosaur("Large Jenny", 25)
        self.robot = Robot("Aluminum Devil")
    
    def run_game(self):
        pass

    def display_welcome(self):
        print(f"Welcome to the death match of the century.\n{self.dinosaur.name} Vs. {self.robot.name}\nWho will survive?")

    def battle_phase(self):
        self.dinosaur.attack(self.robot)

    def display_winner(self):
        pass