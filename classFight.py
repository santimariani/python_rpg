import entities
import time
import random

from classCharacter import Hero, Opponent

class Fight:
    def __init__(self):
        self.name = True
        
    def start_fight(self, hero, opponent):
        print("=-•-==-•-==-•-==-•-=\nA NEW MATCH BEGINS!!\n=-•-==-•-==-•-==-•-=\n")
        time.sleep(2)
        print("The crowd goes WILD!")
        time.sleep(2)
        print()
        print(f"On the left, we have {entities.hero.name}!")
        print()
        entities.hero.print_status()
        time.sleep(5)
        print(f"On the right, we have {entities.matt.name}!")
        print()
        entities.matt.print_status()
        time.sleep(5)
        print("Now... let the match BEGIN!")
        self.run_fight()

    def run_fight(self):
        while entities.matt.health > 0 and entities.hero.health > 0:
            print("You have %d HP and %d SP." % (entities.hero.health, entities.hero.stamina))
            print("%s has %d HP and %d SP." % (entities.matt.name, entities.matt.health, entities.matt.stamina))
            print()
            print("What do you want to do?")
            print()
            print("1. Throw a punch (25% of 1.5x damage) — 5 SP")
            print("2. Attempt a high kick (25% of 2x damage) — 10 SP")
            print("3. Guard & Heal")
            print("4. Use Item")
            print()
            user_input = input()
            if user_input == "1":
                entities.hero.punch(entities.matt)
                if entities.matt.health <= 0:
                    print("%s is knocked out." % entities.matt.name)
                    entities.matt.is_knockout(entities.hero)
                    entities.hero.lvl_evolution()
            elif user_input == "2":
                entities.hero.kick(entities.matt)
                if entities.matt.health <= 0:
                    print("%s is knocked out." % entities.matt.name)
                    entities.matt.is_knockout(entities.hero)
                    entities.hero.lvl_evolution()
            elif user_input == "3":
                entities.hero.do_guard()
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

            if entities.matt.is_alive():
                time.sleep(2)
                # Joker attacks hero
                entities.matt.punch(entities.hero)
                time.sleep(2)
                if entities.hero.health <= 0:
                    print("You are knocked out.")

            


