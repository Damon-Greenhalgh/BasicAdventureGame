""" Player Class
This file contains the player class, which is a child to 
the Entity class.

Methods:
 - level_up()
   Handles when the player character levels up.
   Increases each stat, and sets the new required xp to level up again.
 - edit_xp()
   Edits the current amount of xp the player has.
   If the player xp is greater than or equal to max_xp, level_up() 
   method is called.
 - edit_gold()
   Edits the current amount of gold the player has.
   Cannot fall below 0 gold.

Author: Damon Greenhalgh
"""

# Import/s
from EntityClass import Entity

class Player(Entity):
    
    def __init__(self, stats = ["Entity", 10, 10, 10, 4, 3, 3]):
        Entity.__init__(self, stats[ : 4])
        self.level = 1
        self.xp = 0
        self.max_xp = 100
        self.mp = self.int
        self.max_mp = self.mp
        self.gold = 0

        # Stat Gain per Level
        self.str_gain = stats[4]
        self.dex_gain = stats[5]
        self.int_gain = stats[6]

    def level_up(self):
        """
        This function increases the stats of the player after
        level up.
         - param: None
         - return: None
        """
        self.level += 1
        self.xp = 0
        self.max_xp += self.max_xp

        # Stats Increase
        self.str += self.str_gain
        self.dex += self.dex_gain
        self.int += self.int_gain

        # Update Health
        self.max_hp = (self.str * 10)
        self.hp = self.max_hp    # Full HP

        # Display
        print(f"{self.name} has leveled up!")

    def edit_xp(self, value):
        """
        This function changes the current xp value, also handles
        the player level up.
         - param: int value
         - return: None
        """ 
        self.xp = max(self.xp + value, 0)

        if self.xp >= self.max_xp:    # Player level up
            self.level_up()

    def edit_gold(self, value):
        """
        This function changes the gold value of the entity
         - param: int value
         - return: None
        """
        self.gold = max(self.gold + value, 0)
