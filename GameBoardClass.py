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
        # GUI Element/s
        # self.window = gui.Tk()
        # self.window.title("Adventure Game")    # Title

        # self.width = 650    # Width
        # self.height = 450    # Height
        # self.pad = 20    # Padding

        # self.window.geometry(f"{self.width}x{self.height}")    # Initial size of window
        # self.window.minsize(self.width, self.height)
        # self.window.resizable(0, 0)    # Don't allow for resizing

        # System Element/s
        self.main()
    
    def create_player(self):
        """
        This function creates the player object.
         - param: None
         - return: None
        """
        #Systems
        self.player = None
        name = input("Type in your Adventurer's Name, or type 'Random' for a random name.\nName of Adventurer: ")
        if name == "Random":
            random_names = ["Vex'ahlia", "Grog Strongjaw", "Jester Lavorre", "Vax'ildan", "Keyleth"]
            idx = random.randrange(len(random_names))
            name = random_names[idx]

        self.clear()    # Clear Terminal
        self.pause()    # Pause

        idx = int(input("(Barbarian - 1, Ranger - 2, Wizard - 3)\nChoose your Class: "))

        # Determine Player Class
        idx -= 1
        player_classes = [Barbarian(name), Ranger(name), Wizard(name)]
        self.player = player_classes[idx]

        self.clear()    # Clear Terminal
        self.pause()    # Pause

    def create_enemy(self):
        """
        This function creates the enemy object.
         - param: None
         - return: obj enemy
        """
        list_of_enemies = [Wolf(), Goblin(), Giant_Spider(), Owlbear(), Beholder(), Green_Dragon()]
        idx = random.randrange(len(list_of_enemies))    # Choose an enemy to create.
        enemy = list_of_enemies[idx]
        return enemy

    def combat(self, enemy):
        """
        This function handles all combat systems and calls/
         - param: obj enemy
         - return: None
        """
        print(f"A wild {enemy.name} has appeared!")
        self.pause()    # Delay
        combat = True
        
        while combat:
            action = int(input(f"{self.player.name} HP: ({self.player.hp} / {self.player.max_hp}) - {enemy.name} HP: ({enemy.hp} / {enemy.max_hp})\n\n(Attack - 1, Skills - 2 (DEV), Inventory - 3 (DEV), Flee - 4)\nAction: "))
            self.pause()    # Pause
            self.clear()    # Clear

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
                    skill = int(input(f"{self.player.name}'s Skills:\n({self.player.skills[0]} - 1, {self.player.skills[1]} - 2, {self.player.skills[2]} - 3)\nAction: "))
                    self.player.skill_rage()

                elif action == 3:    # Check Inventory
                    self.in_development()

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

            except EntityDeathError:    # Either the player or the enemy has been slain
                if self.player.hp == 0:    # Player has been slain.
                    print(f"{self.player.name} has been slain!")
                    self.pause()    # Delay

                elif enemy.hp == 0:    # self.player slays the enemy.
                    print(f"{self.player.name} has slain the {enemy.name}!\n{self.player.name} gained {enemy.max_hp} XP and {enemy.max_hp // 4} GOLD!")
                    self.pause()    # Delay
                    self.player.edit_xp(enemy.max_hp)    # Player gains XP
                    self.player.edit_gold(enemy.max_hp // 4)    # Player gains GOLD

                combat = False    # End Combat

            self.pause()

    def stats(self):
        """
        This function displays the players current stats.
         - param: None
         - return: None
        """
        print(f"{self.player.name}'s Stats\nClass: {self.player.player_class}\nLevel {self.player.level}: ({self.player.xp} / {self.player.max_xp})\nHealth: ({self.player.hp} / {self.player.max_hp})\n{self.player.class_stat_name}: ({self.player.mp} / {self.player.max_mp})\nGold: {self.player.gold}\n(STR: {self.player.str} DEX: {self.player.dex} INT: {self.player.int})")

    def in_development(self):
        print("Feature is currently in development!")

    def pause(self):
        """
        This funcion pauses the the game for a brief period.
        """
        time.sleep(0.5)

    def clear(self):
        """
        This function clears the game screen.
         - param: None
         - return: None
        """
        os.system("cls" if os.name == "nt" else "clear")

    def main(self):
        """
        This function handles all calls.
         - param: None
         - return: None
        """
        # GUI (On hold)
        # Console Output Frame
        # self.text_frame = gui.Frame(master = self.window)
        # self.text_frame.place(anchor = "nw", x = self.pad, y = self.pad)

        # self.text = gui.Text(master = self.text_frame, width = 55, height = 20)
        # self.text.pack()

        # Player Input Frame
        # self.entry_frame = gui.Frame(master = self.text_frame)
        # self.entry_frame.pack(side = gui.LEFT)

        # self.button = gui.Button(master = self.entry_frame, text = "Enter", width = 10)
        # self.button.pack(side = gui.RIGHT, padx = self.pad, pady = self.pad)

        # self.entry = gui.Entry(master = self.entry_frame, width = 45)
        # self.entry.pack(side = gui.LEFT, pady = self.pad)

        # Systems
        self.die = Die()
        self.flee_condition = 10
        self.create_player()
        game = True

        # GUI
        # Player Stats Frame
        # self.info_frame = gui.Frame(master = self.window)
        # self.info_frame.place(anchor = "nw", x = self.pad + 468, y = self.pad)

        # self.lbl_name = gui.Label(
        #     master = self.info_frame, 
        #     text = f" {self.player.name} \n The {self.player.self.player_class} ",
        #     font = (None, 17),
        #     justify = gui.LEFT,
        #     relief = gui.GROOVE,
        #     borderwidth = 5,
        #     pady = 8,
        #     fg = "black"
        #     )
        
        # self.lbl_stats = gui.Label(
        #     master = self.info_frame,
        #     text = f"LVL {self.player.level} - {self.player.xp}/{self.player.max_xp}\nHP - {self.player.hp}/{self.player.max_hp}\nMP - {self.player.mp}/{self.player.max_mp}\nGOLD - {self.player.gold}\nSTR - {self.player.str}\nDEX - {self.player.dex}\nINT - {self.player.int}", 
        #     font = (None, 12),
        #     justify = gui.LEFT, 
        #     borderwidth = 5,
        #     pady = 15,
        #     padx = 9,
        #     fg = "black"
        #     )

        # self.lbl_name.pack()
        # self.lbl_stats.pack()

        self.stats()

        while game:

            action = int(input("\n(Battle - 1, View Stats - 2, View Shop - 3 (DEV),  Exit - 4)\nAction: "))
            self.pause()
            self.clear()

            if action == 1:    # Battle
                enemy = self.create_enemy()
                self.combat(enemy)

            elif action == 2:    # View Stats
                self.stats()

            elif action == 3:    # View Shop
                self.in_development()

            elif action == 4:    # Exit game
                game = False
        
        # self.window.mainloop()

game = GameBoard()
