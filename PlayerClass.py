"""
Title: Player Class
Author: Damon Greenhalgh
Description: This file contains the Player Class, which is used to create a player object.
"""

class Player:
    """
    The player class creates a player object.
     - param: int max_heath
     - param: int attack
     - param: list inverntory  
    """
    def __init__(self, name = "Player", level = 1, max_health = 50, max_xp = 10, attack = 5):
        self.__name = name
        self.__level = 1
        self.__max_health = max_health
        self.__health = max_health          # Start at full hp.
        self.__max_xp = max_xp
        self.__xp = 0
        self.__gold = 0
        self.__base_attack = attack
        self.__attack = attack      # Base of 1 dmg

    def __str__(self):
        return "{0}'s Stats:\n\nHealth: ({1} / {2})\nLevel {3} ({4} / {5})\nGold: {6}\nAttack Damage: {7}\n".format(self.__name, self.__health, self.__max_health, self.__level, self.__xp, self.__max_xp, self.__gold, self.__attack)

    """ Returns the respective variable of the player object """
    def get_name(self):
        return self.__name
    def get_level(self):
        return self.__level
    def get_max_health(self):
        return self.__max_health
    def get_health(self):
        return self.__health
    def get_max_xp(self):
        return self.__max_xp
    def get_xp(self):
        return self.__xp
    def get_attack(self):
        return self.__attack
    
    def edit_heath(self, val):
        """
        This function edits the players health.
         - param: int val
         - return: None
        """
        new_health = self.__health + val

        if new_health < 0:                      # If health falls below 0, health is set to 0.
            self.__health = 0

        elif new_health > self.__max_health:    # If health is greater than max health, health is set to max health.
            self.__health = self.__max_health

        else:                                   # Otherwise set health to new value.
            self.__health = new_health

    def edit_xp(self, val):
        """
        This function increases the experience points of the player
        and checks to see if the player has leveled up.
         - param: int val
         - return: None
        """
        self.__xp += val
        if self.__xp >= self.__max_xp:                 # Check if the player has leveled up.
            print("{0} has leveled up!".format(self.__name))
            self.__level += 1 
            self.__max_health += 25
            self.__health = self.__max_health          # Set to full hp.                       
            self.__attack += self.__attack             # Double the players damage.
            self.__xp = 0                              # Reset experience points.
            self.__max_xp += self.__max_xp             # Set new experience points required to level up again.

    def edit_gold(self, val):
        """
        This function adds gold to the player.
         - param: int val
         - return: None
        """
        self.__gold += val

    