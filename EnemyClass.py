"""
Title: Enemy Class
Author: Damon Greenhalgh
Description: This file contains the Enemy Class, which is used to create a enemy object.
"""

class Enemy:
    """
    The enemy class creates an enemy object.
     - param: str name
     - param: int max_health
     - param: int attack
    """
    def __init__(self, name = "Enemy", max_health = 0, attack = 0):
        self.__name = name
        self.__max_health = max_health
        self.__health = max_health
        self.__attack = attack

    def __str__(self):
        return "{0}'s Stats:\nHealth: {1} / {2}\nDamage: {3}".format(self.__name, self.__health, self.__max_health, self.__attack)\

    """ Returns respective variable of the Enemy Object """
    def get_name(self):
        return self.__name
    def get_max_health(self):
        return self.__max_health
    def get_health(self):
        return self.__health
    def get_attack(self):
        return self.__attack

    def edit_heath(self, val):
        """
        This function edits the enemy health.
         - param: int val
        """
        new_health = self.__health + val

        if new_health < 0:                      # If health falls below 0, health is set to 0.
            self.__health = 0

        elif new_health > self.__max_health:    # If health is greater than max health, health is set to max health.
            self.__health = self.__max_health

        else:                                   # Otherwise set health to new value.
            self.__health = new_health
