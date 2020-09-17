""" Entity Class
This file contains the entity class, and is a basis for all
objects within the project.

Methods:
 - attack()
   Handles the attack action of an entity.
 - edit_hp()
   Edits the hp of the entity.

Author: Damon Greenhalgh
"""

# Import/s
from DieClass import Die

class Entity:

    def __init__(self, stats = ["Entity", 10, 10, 10]):
        self.name = stats[0]

        # Stats
        self.str = stats[1]
        self.dex = stats[2]
        self.int = stats[3]

        # Determine the entity's highest statistic.
        stats = stats[1 : ]
        highest_stat = max(stats)
        self.prof = [stats[i] for i in range(len(stats)) if stats[i] == highest_stat][0]
        
        # Calculate Health
        self.hp = (self.str * 10)     
        self.max_hp = self.hp

    def attack(self):    # Basic attack.
        """
        This function handles the attack action of an entity.
         - param: None
         - return: int damage
        """
        die = Die()    # Create Die
        idx = 2
        
        # Roll to hit.
        roll = die.roll()

        # Roll for damage.
        type = min(self.prof // 6, 5)    # Determine the type of die, based on the main stat of the entity.
        rolls = max(self.prof // 6, 1)    # Determine the number of rolls for the type of die.
        damage = die.roll(rolls, type)

        if roll == 1:    # Fumble
            damage = 0 
            idx = 0

        elif (20 - self.dex // 3) <= roll <= 20:    # Critical hit
            damage = damage * 2
            idx = 1

        # Display
        disp_str = ["Fumble! ", "Critical Hit! ", ""]
        print(f"{self.name} rolled a {roll}!\n{disp_str[idx]}{self.name} deals {damage} damage!")
        return damage

    def edit_hp(self, value):
        """
        This function changes the hp value of the entity.
         - param: int value
         - return: None
        """
        new_hp = self.hp + value
        if new_hp <= 0:
            self.hp = 0
        elif new_hp >= self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp = new_hp