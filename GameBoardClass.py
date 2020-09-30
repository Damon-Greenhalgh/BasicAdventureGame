""" GameBoard Class
This file contains the gameboard class. 
This class handles all game systems, and all major calls.

Methods:
 - create_player()
   Creates a player object with respective class.
 - create_enemy()
   Creates a enemy object.
 - combat() (DEV)
   Handles all combat system and calls.
 - stats()
   Displays the statistics of the player character.
 - pause()
 - clear()
 - main()
   Handles all calls to other functions.

 # Developer Note:
GUI implementation via tkinter is planned.

Author: Damon Greenhalgh
"""

# Import/s
import os
import time
import random
import tkinter as gui
from PlayerClassesFile import *
from EnemyClassesFile import *
from ExceptionsClass import *
from DieClass import Die

class GameBoard:

    def __init__(self):
        # System Element/s
        self.main()
    
    def create_player(self):
        """ This function creates the player object. """
        #Systems
        self.player = None

        class_idx = int(input("Choose your Class:\n(Barbarian - 1, Ranger - 2, Wizard - 3)\n>>> ")) - 1    # Get Player Class
        name = input("Type in your Adventurer's Name, or type 'Random' for a random name.\n>>> ")    # Get Player Name

        if name == "Random":    # Generate a random name based on the class.
            random_names = [["Grog", "Mallkaurr", "Jolmasall", "Letho"], ["Vex'ahlia", "Vax'ildan", "Valeria", "Slyvanis"], ["Jester", "Keyleth", "Vogla", "Fiova"]]
            name_idx = random.randrange(len(random_names))
            name = random_names[class_idx][name_idx]

        # Create Player Object
        player_classes = [Barbarian(name), Ranger(name), Wizard(name)]
        self.player = player_classes[class_idx]

    def create_enemy(self):
        """ This function creates the enemy object.
          - return: obj enemy
        """
        list_of_enemies = [Wolf, Goblin, Giant_Spider, Owlbear, Beholder, Green_Dragon]
        idx = random.randrange(len(list_of_enemies))    # Choose an enemy to create.
        enemy = list_of_enemies[idx]()
        return enemy

    def combat(self, enemy):
        """ This function handles all combat systems and calls/
          - param: obj enemy
        """
        print(f"A wild {enemy.name} has appeared!\n")
        combat = True
        
        while combat:
            action = int(input(f"{self.player.name} HP: ({self.player.hp} / {self.player.max_hp}) - {enemy.name} HP: ({enemy.hp} / {enemy.max_hp})\n\n(Attack - 1, Skills - 2 (DEV), Inventory - 3 (DEV), Flee - 4)\n>>> "))

            try:
                # Players Turn
                if action == 1:    # Basic Attack Action
                    damage = self.player.attack()
                    damage = enemy.edit_status(damage)
                    enemy.edit_hp(-damage)

                    # Check if enemy has been slain.
                    if enemy.hp == 0:
                        raise EntityDeathError

                elif action == 2:    # Skills Action
                    skill_idx = int(input(f"{self.player.name}'s Skills:\n({self.player.skills[0][0]} - 1, {self.player.skills[1][0]} - 2, {self.player.skills[2][0]} - 3)\n>>> ")) - 1
                    self.player.skills[skill_idx][1]()    # Call Method
                    print(f"{self.player.name} casts {self.player.skills[skill_idx][0]}!")

                elif action == 3:    # Check Inventory
                    pass

                elif action == 4:    # Flee Action
                    roll = self.die.roll()
                    if roll > self.flee_condition:    # If the player is able to flee, the chance to flee is reduced
                        print(f"{self.player.name} flees!")
                        self.flee_condition = min(self.flee_condition + 1, 20)
                        combat = False
                        break    # End combat
                    else:
                        print(f"{self.player.name} was unable to flee?!")

                # Enemy Turn
                damage = enemy.attack()
                damage = self.player.edit_status(damage)
                self.player.edit_hp(-damage)

                if self.player.hp == 0:
                    raise PlayerDeathError

            except EntityDeathError:    # Enemy has been kiled.
                print(f"{self.player.name} has slain the {enemy.name}!\n{self.player.name} gained {enemy.max_hp} XP and {enemy.max_hp // 4} GOLD!")
                self.player.edit_xp(enemy.max_hp)    # Player gains XP
                self.player.edit_gold(enemy.max_hp // 4)    # Player gains GOLD
                combat = False    # End Combat

            except PlayerDeathError:    # Player has been killed.
                print(f"{self.player.name} has been slain!")
                combat = False    # End Combat

            print()    # Formatting

    def stats(self):
        """ This function displays the players current stats. """
        print(f"{self.player.name}'s Stats\nClass: {self.player.player_class}\nLevel {self.player.level}: ({self.player.xp} / {self.player.max_xp})\nHealth: ({self.player.hp} / {self.player.max_hp})\n{self.player.class_stat_name}: ({self.player.mp} / {self.player.max_mp})\nGold: {self.player.gold}\n(STR: {self.player.str} DEX: {self.player.dex} INT: {self.player.int})")

    def main(self):
        """ This function handles all calls. """
        # Systems
        self.die = Die()
        self.flee_condition = 10
        self.create_player()
        game = True

        self.stats()

        while game:
            action = int(input("\n(Battle - 1, View Stats - 2, View Shop - 3 (DEV),  Exit - 4)\n>>> "))

            if action == 1:    # Battle
                enemy = self.create_enemy()
                self.combat(enemy)

            elif action == 2:    # View Stats
                self.stats()

            elif action == 3:    # View Shop
                pass

            elif action == 4:    # Exit game
                game = False
        

game = GameBoard()
