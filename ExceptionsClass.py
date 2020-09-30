""" Exception Classes
This file contains exception classes.

Classes:
 - EntityDeathError

Author: Damon Greenhalgh
"""

class EntityDeathError(Exception):
    """ Raised when an entity dies during combat. """
    pass

class PlayerDeathError(Exception):
    """ Raised when the player dies during combat. """
    pass
