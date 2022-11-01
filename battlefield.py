from dinosaur import Dinosaur
from robot import Robot



class Battlefield():
    def __init__(self):
        self.dinosaur_fighter = Dinosaur("Large Jenny", 25)
        self.robot_fighter = Robot("Aluminum Cowboy")
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        

    def display_welcome(self):
        print(f"Welcome to the death match of the century.\n{self.dinosaur_fighter.name} Vs. {self.robot_fighter.name}\nWho will survive?")

    def choose_robots_weapon(self):
        weapon_chosen = False
        while weapon_chosen == False:
            weapon_choice = input(f"Which weapon should {self.robot_fighter.name} use? {self.robot_fighter.active_weapon[0].name}, {self.robot_fighter.active_weapon[1].name}, or {self.robot_fighter.active_weapon[2].name}? ")
            if weapon_choice == self.robot_fighter.active_weapon[0].name:
                self.robot_fighter.attack(self.dinosaur_fighter)
                weapon_chosen = True
            elif weapon_choice == self.robot_fighter.active_weapon[1].name:
                self.robot_fighter.attack_2(self.dinosaur_fighter)
                weapon_chosen = True
            elif weapon_choice == self.robot_fighter.active_weapon[2].name:
                self.robot_fighter.attack_3(self.dinosaur_fighter)
                weapon_chosen = True


    def battle_phase(self):
        
        while self.dinosaur_fighter.health > 0 and self.robot_fighter.health > 0:
            self.dinosaur_fighter.attack(self.robot_fighter)
            print(f"{self.robot_fighter.name} has {self.robot_fighter.health} health left!")
            if self.robot_fighter.health <= 0:
                self.display_winner()
                break  
            self.choose_robots_weapon()
            print(f"{self.dinosaur_fighter.name} has {self.dinosaur_fighter.health} health left!")
            if self.dinosaur_fighter.health <= 0:
                self.display_winner()
                break
                 


    def display_winner(self):
        if self.dinosaur_fighter.health <= 0:
            print(f"{self.dinosaur_fighter.name} has no health left! They've been defeated!\n{self.robot_fighter.name} WINS!!!")
        else:
            print(f"{self.robot_fighter.name} has no health left! They've been defeated!\n{self.dinosaur_fighter.name} WINS!!!")