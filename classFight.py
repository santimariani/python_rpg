# Add: While guarding, have Defense and Reflexes go up  25%.
# Add: Agility and reflexes combined influence critical blow chances


import entities
import time
import random

class Fight:
    def __init__(self):
        self.name = True
        
    def start_fight(self, hero, opponent):
        print("=-•-==-•-==-•-==-•-=\n*A NEW MATCH BEGINS*\n=-•-==-•-==-•-==-•-=\n")
        time.sleep(2)
        print("The crowd goes WILD!")
        time.sleep(2)
        print()
        print(f"On the left, we have {hero.name}!")
        print()
        hero.print_status()
        time.sleep(2)
        print(f"On the right, we have {opponent.name}!")
        print()
        opponent.print_status()
        time.sleep(2)
        print("Now... let the match BEGIN!")
        self.run_fight(hero, opponent)

    def run_fight(self, hero, opponent):
        while opponent.health > 0 and hero.health > 0:
            print("You have %d HP and %d SP." % (hero.health, hero.stamina))
            print("%s has %d HP and %d SP." % (opponent.name, opponent.health, opponent.stamina))
            print()
            print("What do you want to do?")
            print()
            print("1. Throw a punch (25% chance of 2x damage) — 5 SP")
            print("2. Attempt a high kick (50% chance of 3x damage) — 15 SP")
            print("3. Guard & Heal")
            print("4. Use Item")
            print()
            user_input = input("> ")
            if user_input == "1":
                hero.punch(opponent)
                if opponent.health <= 0:
                    print("%s is knocked out." % opponent.name)
                    opponent.is_knockout(hero)
                    hero.lvl_evolution()
            elif user_input == "2":
                hero.kick(opponent)
                if opponent.health <= 0:
                    print("%s is knocked out." % opponent.name)
                    opponent.is_knockout(hero)
                    hero.lvl_evolution()
            elif user_input == "3":
                hero.do_guard()
            elif user_input == "4":
                pass
    #             if hero.items == False:
    #                 print("You have no items")
    #             else:
    #                 print(f"Which of your items would you like to use? \n{hero.items}")
    #                 answer = input().lower()
    #                 if answer == "tonic":
    #                     tonic.do_apply()
    #                 elif answer == "sword":
    #                     sword.do_apply()
    #                 elif answer == "elixir":
    #                     elixir.do_apply()
            else:
                print("Invalid input %r" % user_input)

            if opponent.is_alive():
                time.sleep(2)
                opponent.punch(hero)
                time.sleep(2)
                if hero.health <= 0:
                    print("You are knocked out!\n")
