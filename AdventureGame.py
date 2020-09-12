"""
Title: Basic Adventure Game
Author: Damon Greenhalgh
Description: This is a basic adventure game.

Key Features:
 - Combat (with various enemies)
 - Loot (aquire different items that alter stats)

 Plans:
 - Implement healing system.
 - Implement shop system.
 - Contextual dialogue system.
 - Critical Hit system.
"""

# Imports
import os
import math
import random
from PlayerClass import Player
from EnemyClass import Enemy

def combat(player = Player()):
    """
    Handles all combat calls and systems.
     - param: obj player
     - return: None
    """
    enemy = create_enemy()    # Create enemy object.
    in_combat = True          # Loop variable
    rewards = [0, 0]          # [int gold, int xp]

    while in_combat:
        print("{0} - Health: ({1} / {2})".format(enemy.get_name(), enemy.get_health(), enemy.get_max_health()))       # Display Player Health and Damage
        print("{0} - Health: ({1} / {2})".format(player.get_name(), player.get_health(), player.get_max_health()))    # Display Player Health and Damage
        action = int(input("\n(Attack - 1, Inventory - 2, Flee - 3)\nAction: "))                                      # Get player action
        clear()    # Clear game board

        # Battle Actions
        if action == 1:    # Player  attacks

            # Player attacks the enemy.
            player_lbound = max(1, math.floor(player.get_attack() - (1/4) * player.get_attack()))                 # Lower bound
            player_hbound = max(2, math.floor(player.get_attack() + (1/4) * player.get_attack()))                 # Higher bound
            player_dmg = random.randrange(player_lbound, player_hbound)                                           # Generate random player damage.
            enemy.edit_heath(-player_dmg)                                                                         # Player deals damage to the enemy.
            print("You swing your sword at the {0} and deal {1} damage!".format(enemy.get_name(), player_dmg))    # Display combat dialogue
            
            # Enemy attacks the player.
            enemy_lbound = max(1, math.floor(enemy.get_attack() - (1/4) * enemy.get_attack()))                    # Lower bound
            enemy_hbound = max(2, math.floor(enemy.get_attack() + (1/4) * enemy.get_attack()))                    # Higher bound
            enemy_dmg = random.randrange(enemy_lbound, enemy_hbound)                                              # Generate random enemy damage.
            player.edit_heath(-enemy_dmg)                                                                         # Enemy deals damage to the player.
            print("The {0} fights back! Dealing {1} damage!".format(enemy.get_name(), enemy_dmg))                 # Display combat dialogue


        # Exit Conditions
        if player.get_health() == 0:     # Player faints
            print("You have fainted!")
            in_combat = False

        elif enemy.get_health() == 0:    # Enemy faints
            rewards[0] = max(1, math.floor(enemy.get_max_health() * (1/4)))    # Set gold reward
            rewards[1] = enemy.get_max_health()                                # Set experience reward
            print("The {0} faints! You gain {1} gold and {2} xp!".format(enemy.get_name(), rewards[0], rewards[1]))
            player.edit_gold(rewards[0])
            player.edit_xp(rewards[1])
            in_combat = False

        elif action == 3:    # Flee action
            print("You flee, with you tail between your legs.")
            in_combat = False

        print()

    return rewards
        
def create_player():
    """
    Creates and returns a player object.
     - param: None
     - return: obj player
    """
    player_name = input("Insert Player Name: ")
    player = Player(player_name)
    clear()   # Clear game board

    return player

def create_enemy():
    """
    Creates and returns an enemy object.
     - param: None
     - return: obj enemy
    """
    enemy_varaints = [("Mouse", 2, 1), ("Gnoll", 5, 2), ("Goblin", 10, 3), ("Troll", 50, 10), ("Giant", 100, 25), ("Dragon", 500, 100)]     # Enemy variants, with different preset stats. ("name", max_health, attack_damage)
    val = random.randrange(0, len(enemy_varaints))

    enemy = Enemy(enemy_varaints[val][0], enemy_varaints[val][1], enemy_varaints[val][2])     # Create Enemy object.
    return enemy

def clear():
    """ Clears the game boad """
    os.system("cls")

def main():
    """ Handles all calls to other functions. """
    player = create_player()    # Create Player
    game = True

    while game:
        action = int(input("What would you like to do?\n(Battle - 1, View Stats - 2, Exit - 3)\nAction: "))
        clear()   # Clear game board
        if action == 1:      # Fight
            combat(player)

        elif action == 2:    # View stats
            print(player)

        elif action == 3:    # End game
            game = False

main()

