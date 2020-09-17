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
         - return: obj player
        """
        #Systems
        player = None
        name = input("Name of Adventurer: ").upper()
        self.clear()    # Clear Terminal
        player_class = int(input("(Barbarian - 1, Ranger - 2, Wizard - 3)\nChoose your Class: "))
        self.clear()    # Clear Terminal

        # Determine Player Class
        if player_class == 1:
            player = Barbarian(name)
        elif player_class == 2:
            player = Ranger(name)
        elif player_class == 3:
            player = Wizard(name)

        return player

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

    def combat(self, player, enemy):
        """
        This function handles all combat systems and calls/
         - param: obj player
         - param: obj enemy
         - return: None
        """
        print(f"A wild {enemy.name} has appeared!")
        self.pause()    # Delay
        combat = True

        while combat:
            action = int(input(f"{player.name} HP: ({player.hp} / {player.max_hp}) - {enemy.name} HP: ({enemy.hp} / {enemy.max_hp})\n\n(Attack - 1, Skills - 2 (DEV), Inventory - 3 (DEV), Flee - 4)\nAction: "))
            self.clear()
            
            if action == 1:    # Attack Action
                try:
                    entity = sorted([player, enemy], key = lambda x : -x.dex)    # Highest dex.
                    a, b = 0, 1

                    for i in range(2):
                        damage = entity[a].attack()
                        entity[b].edit_hp(-damage)

                        # Check if entity[b] has died.
                        if entity[b].hp == 0:
                            raise EntityDeathError

                        a, b = b, a    # Swap

                except EntityDeathError:
                    if player.hp == 0:    # Player has been slain.
                        print(f"{player.name} has been slain!")
                        self.pause()    # Delay

                    elif enemy.hp == 0:    # Player slays the enemy.
                        print(f"{player.name} has slain the {enemy.name}!\n{player.name} gained {enemy.max_hp} XP and {enemy.max_hp // 4} GOLD!")
                        self.pause()    # Delay
                        player.edit_xp(enemy.max_hp)    # Player gains XP
                        player.edit_gold(enemy.max_hp // 4)    # Player gains GOLD

                    combat = False    # End Combat

            elif action == 2:    # Skills Action
                pass

            elif action == 3:    # Check Inventory
                pass

            elif action == 4:    # Flee Action
                print(f"{player.name} flees!")
                combat = False
            
            self.pause()

    def stats(self, player):
        """
        This function displays the player's current stats.
         - param: obj player
         - return: None
        """
        print(f"{player.name}'S STATS\nLVL {player.level}: ({player.xp} / {player.max_xp})\nHP: ({player.hp} / {player.max_hp})\n{player.class_stat_name}: ({player.mp} / {player.max_mp})\nGOLD: {player.gold}\nSTR: {player.str} DEX: {player.dex} INT: {player.int}")

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
        player = self.create_player()
        game = True

        # GUI
        # Player Stats Frame
        # self.info_frame = gui.Frame(master = self.window)
        # self.info_frame.place(anchor = "nw", x = self.pad + 468, y = self.pad)

        # self.lbl_name = gui.Label(
        #     master = self.info_frame, 
        #     text = f" {player.name} \n The {player.player_class} ",
        #     font = (None, 17),
        #     justify = gui.LEFT,
        #     relief = gui.GROOVE,
        #     borderwidth = 5,
        #     pady = 8,
        #     fg = "black"
        #     )
        
        # self.lbl_stats = gui.Label(
        #     master = self.info_frame,
        #     text = f"LVL {player.level} - {player.xp}/{player.max_xp}\nHP - {player.hp}/{player.max_hp}\nMP - {player.mp}/{player.max_mp}\nGOLD - {player.gold}\nSTR - {player.str}\nDEX - {player.dex}\nINT - {player.int}", 
        #     font = (None, 12),
        #     justify = gui.LEFT, 
        #     borderwidth = 5,
        #     pady = 15,
        #     padx = 9,
        #     fg = "black"
        #     )

        # self.lbl_name.pack()
        # self.lbl_stats.pack()

        self.stats(player)

        while game:

            action = int(input("\n(Battle - 1, View Stats - 2, View Shop - 3 (DEV),  Exit - 4)\nAction: "))
            self.pause()
            self.clear()

            if action == 1:    # Battle
                enemy = self.create_enemy()
                self.combat(player, enemy)

            elif action == 2:    # View Stats
                self.stats(player)

            elif action == 3:    # View Shop
                pass

            elif action == 4:    # Exit game
                game = False
        
        # self.window.mainloop()

game = GameBoard()
