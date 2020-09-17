""" EnemyClasses File
This file contains multiple enemy classes. Each class contains
an outline for an enemy monster with custom name and stats.

Classes: (DEV)
 - Wolf
 - Goblin
 - Giant_Spider
 - Owlbear
 - Beholder
 - Green_Dragon

 Author: Damon Greenhalgh
"""

# Import/s
from EntityClass import Entity

# List of enemies.
# Wolf, Goblin, Giant Spider, Owlbear, Beholder, Green Dragon
class Mouse(Entity):
    def __init__(self):
        stats = ["Mouse", 1, 3, 1]    # 5 Total
        Entity.__init__(self, stats)

class Wolf(Entity):
    def __init__(self):
        stats = ["Wolf", 2, 10, 3]    # 15 Total
        Entity.__init__(self, stats)

class Goblin(Entity):
    def __init__(self):
        stats = ["Goblin", 4, 10, 6]    # 20 Total
        Entity.__init__(self, stats)

class Giant_Spider(Entity):
    def __init__(self):
        stats = ["Giant Spider", 10, 22, 8]    # 30 Total
        Entity.__init__(self, stats)

class Owlbear(Entity):
    def __init__(self):
        stats = ["Owlbear", 25, 8, 12]    # 45 Total
        Entity.__init__(self, stats)

class Beholder(Entity):
    def __init__(self):
        stats = ["Beholder", 30, 12, 23]    # 65 Total
        Entity.__init__(self, stats)

class Green_Dragon(Entity):
    def __init__(self):
        stats = ["Green Dragon", 45, 20, 25]    # 90 Total
        Entity.__init__(self, stats)

class Astral_Drednaught(Entity):
    def __init__(self):
        stats = ["Astral Drednaught", 65, 10, 45]    # 120 Total
        Entity.__init__(self, stats)
