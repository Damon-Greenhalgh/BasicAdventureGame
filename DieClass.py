""" Die Class
This file contains the die class.

Methods:
 - roll()
   Rolls dice based on various parameters

Author: Damon Greenhalgh
"""

import math
import random

class Die:

    def roll(self, num_rolls = 1, idx = 5, advantage = False, disadvantage = False):
        """
        This function rolls types of die.
         - param: int idx
         - param: int num_rolls
         - param: bool advantage
         - param: bool disadvantage
         - return: int roll
        """
        types = [4, 6, 8, 10, 12, 20]    # Contians the types of die.
        roll_sum = 0
        while num_rolls != 0:   
            roll = random.randrange(1, types[idx] + 1)    # Roll

            if advantage:    # Roll with advantage.
                roll2 = random.randrange(1, types[idx] + 1)
                roll_sum += max(roll, roll2)

            elif disadvantage:    # Roll with disadvantage.
                roll2 = random.randrange(1, types[idx] + 1)
                roll_sum += min(roll, roll2)

            else:
                roll_sum += roll    # Add to sum.
            
            num_rolls -= 1

        return roll_sum    # Return the sum of rolls.