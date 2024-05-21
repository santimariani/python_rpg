import time

from classDay import Day
from tools import slow_print
import entities

class Engine:
    def __init__(self):
        self.start_day = Day()
        
    def begin_game(self):
        x = False
        while x == False:
            user_input = input("PRESS Y TO BEGIN:\n> ").lower()
            if user_input == "y":
                self.boot_up_game()
                x = True
            elif user_input == "s":
                self.skip_intro()
                self.start_day.run_day()
                x = True
            else:
                print("Incorrect entry! Try again.")
                x = False
    
    def skip_intro(self):
        entities.hero.name = input("Name: ")
        entities.hero.health = int(input("Health: "))
        entities.hero.max_health = entities.hero.health
        entities.hero.stamina = int(input("Stamina: "))
        entities.hero.max_stamina = entities.hero.stamina
        entities.hero.power = input("Power: ")
        entities.hero.defence = int(input("Defence: "))
        entities.hero.agility = int(input("Agility: "))
        entities.hero.reflexes = int(input("Reflexes: "))
        entities.hero.coins = int(input("Coins: "))
        print()
        entities.hero.print_status()
    
    def boot_up_game(self):
        print()
        slow_print("Booting up game...")
        print()
        time.sleep(2)
        slow_print("\n...\n...\n...\n")
        print()
        time.sleep(2)
        print("File acquired.")
        time.sleep(1)
        print("Unnecessary drama uploaded.")
        time.sleep(1)
        print("Incoming in-your-face title detected.")
        print()
        time.sleep(2)
        slow_print("So let's get this party started...!", 0.1)
        print()
        time.sleep(2)
        print()
        print("=-•-==-•-==-•-==-•-=\n100 DAYS TO VICTORY!\n=-•-==-•-==-•-==-•-=")
        print()
        time.sleep(2)
        print("Get started?\n\n 1 — Yes\n 2 - Duh! \n\nAnswer: ")
    
        opening_answered = False
        while opening_answered == False:
            user_input = input()
            if user_input == "1":
                opening_answered == True
                self.give_intro()
            elif user_input == "2":
                opening_answered == True
                self.give_intro()
            else:
                print("No other way other than forward. Try again!")
                
    def give_intro(self):
        print("\n=-•-==-•-==-•-=\n INTRODUCTION\n=-•-==-•-==-•-=\n")
        slow_print("You have 100 days...\n", 0.1)
        time.sleep(2)
        print()
        print("100 days to train and rise above all the rest!")
        time.sleep(2)
        print("100 days to prove your worth in the ring!")
        time.sleep(2)
        print("100 days to bring down the World Champion and take his place!")
        time.sleep(3)
        print()
        print("Each day, you will have six options, each with its own benefits,\nso that you may become equiped for the task at hand.")
        print()
        time.sleep(6)
        print("YOUR GOAL: qualify to enter the three available tournaments, \nand so earn your right to challenge the Champion himself.")
        print()
        time.sleep(6)
        print("It will not be easy. But then again, attaining glory never has been!")
        print()
        time.sleep(3)
        slow_print("Now, no more stalling. Time to...", 0.1)
        print()
        self.create_character()
   
    def create_character(self):
        print("\n=-•-==-•-==-•-==-•-=\nCREATE YOUR CHARACTER\n=-•-==-•-==-•-==-•-=\n")
        print("To create your character, you must understand the three main attributes: ")
        time.sleep(3)
        print()
        
        print("ENDURANCE — determined by your HEALTH & STAMINA POINTS (HP & SP), both needed to endure battle.")
        time.sleep(5)
        print("STRENGTH - determined by your POWER & DEFENCE SKILLS, used to calculate damage.")
        time.sleep(5)
        print("SWIFTNESS - determined by your AGILITY & REFLEXES SKILLS, used to see whether your attacks hit your foe.")
        time.sleep(5)
        print()
        
        print("With each damage taken, your HEALTH is reduced.")
        time.sleep(3)
        print("Once it reaches zero, you are knocked out!")
        time.sleep(4)
        print()
        
        print("With each attack performed, your STAMINA is spent.")
        time.sleep(3)
        print("Deplete it completely, and you will be unable to perform an attack!")
        time.sleep(4)
        print()
        
        print("The greater your POWER, the greater the possible damage you deal out.")
        time.sleep(3)
        print("The greater your DEFENCE, the greater the possible damage you endure.")
        time.sleep(4)
        print()
        
        print("A higher AGILITY will increase your chances of landing a hit,")
        time.sleep(3)
        print("while higher REFLEXES will allow you to more easily evade a blow.")
        time.sleep(4)
        print()
        
        print("When guarding, DEFENCE will influce the HP raised.")
        time.sleep(3)
        print("Similarly, REFLEXES will do the same for your SP.")
        time.sleep(4)
        print()
        
        print("You are now at LEVEL 1, and currently have:\n")
        print(" * 25 HP and 25 SP.")
        print(" * 5 points for each of your SKILLS.\n")
        print("You also can distribute:")
        time.sleep(3)
        print()
        print(" * 50 ENDURANCE POINTS between your HEALTH & STAMINA.")
        time.sleep(3)
        print(" * 12 SKILL POINTS among each of your six SKILLS.")
        time.sleep(4)
        print()
        
        print("As you gain EXPERIENCE and LEVEL UP:")
        time.sleep(3)
        print()
        print(" * You will be awarded 10 extra ENDURANCE POINTS")
        time.sleep(3)
        print(" * And 4 extra SKILL POINTS")
        time.sleep(2)
        print()
        print("... to apply as you best see fit!")
        time.sleep(3)
        print()
        
        slow_print("So, then, what is your...", 0.1)
        print()
        time.sleep(1)
        print("\n=-•-==-•-==-•-==-•-=\n CHARACTER'S NAME?\n=-•-==-•-==-•-==-•-=")

        entities.hero.name = input("> ")
        print(f"\n{entities.hero.name} — a true warrior's name!")
        time.sleep(1)
        print()
        slow_print(f"Now let's decide on {entities.hero.name}'s stats...", 0.1)
        time.sleep(1)
        print()
        print("\n=-•-==-•-==-•-=\nCHARACTER STATS\n=-•-==-•-==-•-=")
        print()
        print("Let's begin with your overall ENDURANCE. You have 50 POINTS available. So, then... \n")
        time.sleep(3)
        math_works = 0
        while math_works == False:
            setting_health = int(input("How many do you want for HEALTH?\n> "))
            setting_stamina = int(input("How many do you want for STAMINA?\n> "))
            if setting_health + setting_stamina > 50:
                print("That's more than 50! Let's try again.")
                print()
                math_works = False
            elif setting_health + setting_stamina < 50:
                print("That's less than 50! Let's try again.")
                print()
                math_works = False
            else:
                redo_endurance = input(f"\nYou have chosen:\n\n * {setting_health} for HEALTH\n * {setting_stamina} for STAMINA\n\n1 — REDO\n2 — ACCEPT!\n> ")
                if redo_endurance == "1":
                    math_works = False
                elif redo_endurance == "2":
                    math_works = True
                else:
                    print("That is an incorrent entry. Let's try again!\n")
                    math_works = False
                    
        entities.hero.health += setting_health
        entities.hero.max_health = entities.hero.health
        entities.hero.stamina += setting_stamina
        entities.hero.max_stamina = entities.hero.stamina

        print(f"\nWell done! {setting_health} for HEALTH and {setting_stamina} for STAMINA it is!\n")
        time.sleep(3)
        print("Now let's move on to your SKILLS...")
        time.sleep(2)
        print("\nYou have 12 POINTS available to spread among: \n\n * POWER & DEFENCE for your overall STRENGTH, \n * AGILITY & REFLEXES for your overall SWIFTNESS.")
        print()
        time.sleep(5)
        slow_print("So, then...", 0.1)
        print()
        print()
        math_works = 0
        while math_works == False:
            setting_power = int(input("How many do you want for POWER?\n> "))
            setting_defence = int(input("How many do you want for DEFENCE?\n> "))
            setting_agility = int(input("How many do you want for AGILITY?\n> "))
            setting_reflexes = int(input("How many do you want for REFLEXES?\n> "))

            if setting_power + setting_defence + setting_agility + setting_reflexes > 12:
                print("\nThat's more than 12! Let's try again.")
                print()
                math_works = False
            elif setting_power + setting_defence + setting_agility + setting_reflexes < 12:
                print("\nThat's less than 12! Let's try again.")
                print()
                math_works = False
            else:
                redo_endurance = input(f"\nYou have chosen:\n\n * {setting_power} for POWER,\n * {setting_defence} for DEFENCE, \n * {setting_agility} for AGILITY,\n * {setting_reflexes} for REFLEXES.\n\n1 — REDO\n2 — ACCEPT!\n> ")
                if redo_endurance == "1":
                    math_works = False
                elif redo_endurance == "2":
                    math_works = True
                else:
                    print("That is an incorrent entry. Let's try again!\n")
                    math_works = False
         
        entities.hero.power += setting_power
        entities.hero.defence += setting_defence
        entities.hero.agility += setting_agility
        entities.hero.reflexes += setting_reflexes
        
        print("\nCONGRATULATIONS! \n\nHere are your starting stats:")
        time.sleep(3)
        print()
        print(f" * MAX HEALTH: {entities.hero.max_health}")
        print(f" * MAX STAMINA: {entities.hero.max_stamina}")
        print(f" * POWER: {entities.hero.power}")
        print(f" * DEFENCE: {entities.hero.defence}")
        print(f" * AGILITY: {entities.hero.agility}")
        print(f" * REFLEXES: {entities.hero.reflexes}")
        time.sleep(5)
        print()
        slow_print("And now may the adventure begin...\n", 0.1)
        print()
        self.start_day.run_day()
