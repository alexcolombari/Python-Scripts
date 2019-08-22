import os
import sys
import time
import random
from monster import Monster
from personagem import Personagem

def player_health_loss(player_health):
    return initial_player_health - monster_damage

def turns():
    actual_turn = 0
    max_turn = 10

    for turn in range(0, max_turn):
        actual_turn += 1

    return actual_turn, max_turn

def game_function():
    os.system('cls' if os.name == 'nt' else 'clear')

    player_damage = random.randint(3, 15)
    monster_damage = random.randint(3, 15)

    player = Personagem(50, player_damage)
    monster = Monster(100, monster_damage)
    player_health = player.health
    monster_health = monster.health

    while player_health > 0:
        print('Player Health {}\nMonster Health {}\n').format(player_health, monster_health)
        i = raw_input("Press a -> attack / s -> shop / p -> Potion / quit -> exit: ")
        if i == 'quit':
            break
        if i == 'a':
            print("\nYou've attacked the monster within {} damage\n").format(player.damage)
            monster_health -= player.damage
            if monster_health <= 0:
                print("[INFO] Monster died, you've won this game!\n")
                print("[INFO] Backing to main menu...")
                time.sleep(5)
                main()
        if i == 'p':
            if player_health >= 85:
                print("\n[INFO] You don't need it\n")
            else:
                player_health += 15
        if i == '':
            pass
        else:
            print('error')
    

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("[INFO] Commands:\nDigit 'start' to start playing or 'quit' to exit")
    if sys.version_info == 3:
        i = input('Command: ')
        if i == 'quit':
            sys.exit(1)
        elif i == 'start':
            game_function()
        else:
            raise ValueError

    else:
        i = raw_input('Command: ')
        if i == 'quit':
            sys.exit(1)
        elif i == 'start':
            game_function()
        else:
            raise ValueError


if __name__ == '__main__':
    main()