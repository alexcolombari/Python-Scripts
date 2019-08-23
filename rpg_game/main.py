import os
import sys
import time
import random

from monster import Monster
from personagem import Personagem

    player_damage = random.randint(3, 15)
    monster_damage = random.randint(3, 15)

    player = Personagem(100, player_damage)
    monster = Monster(100, monster_damage)
    player_health = player.health
    monster_health = monster.health

    monster_count = 0
    gold = 0

def clearScreen():
    return os.system('cls' if os.name == 'nt' else 'clear')

def shop(gold, player_damage,):
    clearScreen()
    
    while True:
        print("Welcome to store, what do you want do buy?: ")
        buy = input("\n1 -> Health Potion (heals 15) - 10 gold\n2 -> Shield (5 percent less incoming damage) - 25 gold\n\
    3 -> Power up buff (10 percent more damage) - 15 gold\n4 -> Exit shop")
        try:
            if buy == 1:
                print('1')
            elif buy == 2:
                print("2")
            elif buy == 3:
                print("3")
            elif buy == 4:
                break
        except:
            print("Error")



# MAIN GAME FUNCTION
def game_function():
    clearScreen()
    rounds = 1
    max_rounds = input("Enter with the maximum number of monster do you want to fight: ")

    while player_health > 0:
        print('Round {}/{}\nGold: {}\nPlayer Health {}\nMonster Health {}\n').format(rounds, max_rounds, gold, player_health, monster_health)
        i = raw_input("Press a -> attack / s -> shop / p -> Potion / quit -> exit: ")
        if i == 'quit':
            break
        elif i == 'a':
            player_damage = random.randint(3, 15)
            monster_damage = random.randint(3, 15)
            
            print("\nYou've attacked the monster with {} damage\n").format(player_damage)
            monster_health -= player_damage
            
            time.sleep(2)
            
            print("\nYou've been attacked by monster with {} damage\n").format(monster_damage)
            player_health -= monster_damage

            time.sleep(2)

            if player_health <= 0:
                print("You died!")
                time.sleep(3)
                main()
            
            if monster_health <= 0:
                print("[INFO] Monster died, wait for next one!\n")
                rounds += 1
                gold += random.randint(5, 20)
                monster_health = 100
                time.sleep(3)
                if rounds > max_rounds:
                    print("You've won this game, backing to main menu...")
                    time.sleep(5)
                    main()
        elif i == 'p':
            if player_health >= 85:
                print("\n[INFO] You don't need it\n")
            else:
                player_health += 15
        elif i == '':
            pass
        elif i == 's':
            shop(gold)
        else:
            print('error')
    

def main():
    clearScreen()
    
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
