import time
import random
import entities
from tools import slow_print

from classCharacter import Hero, Opponent
from classFight import Fight


class Day:
    def __init__(self):
        self.count = 1
        self.day_part = 1
        self.fight = Fight()
        self.trained = False
        self.bathed = False
        self.sparred = False
        self.competed = False

    def morning_boost(self):
        print("You sleep through the night and wake up to a NEW DAY!\n")
        time.sleep(2)
        probability = random.random()
        if probability > 0 and probability < 0.05:
            print(f"You slept AMAZINGLY well!")
            time.sleep(2)
            print("Your HEALTH and STAMINA were fully restored.\n")
            entities.hero.heal_hp(int(entities.hero.max_health))
            entities.hero.heal_sp(int(entities.hero.max_stamina))
        elif probability > 0.05 and probability < 0.25:
            print(f"You slept soundly.")
            time.sleep(2)
            print("Your HEALTH and STAMINA were restored 50%.\n")
            entities.hero.heal_hp(int(0.75 * entities.hero.max_health))
            entities.hero.heal_sp(int(0.75 * entities.hero.max_stamina))
        elif probability > 0.25 and probability < 0.75:
            print(f"You slept decently well.")
            time.sleep(2)
            print("Your HEALTH and STAMINA were restored 25%.\n")
            entities.hero.heal_hp(int(0.50 * entities.hero.max_health))
            entities.hero.heal_sp(int(0.50 * entities.hero.max_stamina))
        elif probability > 0.75 and probability < 0.90:
            print(f"You woke up multiple times during the night.")
            time.sleep(2)
            print("Your HEALTH and STAMINA were restored 10%.\n")
            entities.hero.heal_hp(int(0.25 * entities.hero.max_health))
            entities.hero.heal_sp(int(0.25 * entities.hero.max_stamina))
        else:
            print(f"You tossed and turned ALL night long...")
            time.sleep(2)
            print("Your HEALTH and STAMINA decreased 25%.\n")
            entities.hero.health -= (int(0.25 * entities.hero.max_health))
            if entities.hero.health < 0:
                entities.hero.health = 1
            entities.hero.stamina -= (int(0.25 * entities.hero.max_stamina))
            if entities.hero.health < 0:
                entities.hero.health = 1
        time.sleep(2)
        entities.hero.print_status()
        print(f"You are at LEVEL {entities.hero.lvl} and have {entities.hero.xp} XP.\n")
        print(f"To LEVEL UP, you need the following XP:\n")
        print("LVL 2 — 50 • LVL 3 - 125 • LVL 4 - 225 • LVL 5 - 350 • LVL 6 - 500 • LVL 7 - 675")
        print("LVL 8 - 875 • LVL 9 - 1100 • LVL 10 - 1450 • LVL 11 - 1825 • LVL 12 (MAX) - 2225")
        print()
        print(f"You have {entities.hero.coins} COINS.\n")
        time.sleep(2)

    def run_day(self):
        while self.count < 101:
            if self.day_part == 1:
                self.morning_boost()
                print(f"It is now DAY {self.count} in the morning. What would you like to do?\n")
                time.sleep(2)
                self.select_action()
                self.day_part = 2
            elif self.day_part == 2:
                print(f"It is now Day {self.count} in the afternoon. What would you like to do?\n")
                time.sleep(2)
                self.select_action()
                self.day_part = 3
            else:
                print(f"It is now Day {self.count} in the evening. What would you like to do?\n")
                time.sleep(2)
                self.select_action()
                self.day_part = 1
                self.trained = False
                self.sparred = False
                self.bathed = False
                self.competed = False
                time.sleep(1)
                self.count += 1
                days_left = int(101 - self.count)
                slow_print(f"Another day comes to an end... Only {days_left} days remaining.\n", 0.1)
                print()
                print(f"=-•-==-•-==-•-=\n END OF DAY {self.count}\n=-•-==-•-==-•-=\n")
        print(f"It is now Day 101. \n\nYour efforts were valiant, but not up to task. \n\nYet experience was gained, and there is always that next try!\n\n Here are your ending stats: \n\n {hero.print_status()}.")
    
    def select_action(self):
        options = """Here are your options:

  1. Eat a meal ------------- restores 25 HP (cost - 5 COINS)
  2. Take a cold bath ------- restores 25 SP (cost - 5 COINS)
 
  3. Go work —--------------- gain 5 COINS 
  4. Exercise at home ------- gain 5 XP (once / day)
 
  5. Go shopping ------------ buy items
  6. Use item --------------- if applicable
 
  7. Spar at the gym -------— win 25 XP? (cost - 5 COINS; once / day)
  8. Fight in a tournament--- advance in the leagues? (once / day)
 
  9. Read notes ------------- review what you have learned so far
 10. Go to bed early -------- increase your chances of better sleep
 """
        
        answered = False
        while answered == False:
            print(options)
            answer = int(input("> "))
            if answer == 1:
                if entities.hero.coins < 5:
                    print("You go to the store for the ingredients only to realize you don't have enough cash. Nothing a quick gig can't fix!\n")
                    answered = True
                else:
                    self.eat()
                    answered = True
            elif answer == 2:
                if entities.hero.coins < 5:
                    print("You go to the store to buy ice only to realize you don't have enough cash. Nothing a quick gig can't fix!\n")
                    answered = True
                else:
                    self.bath()
                    answered = True
            elif answer == 3:
                self.work()
                answered = True
            elif answer == 4:
                self.train()
                self.trained = True
                answered = True
            elif answer == 5:
                self.shop()
                answered = True
            elif answer == 7:
                self.spar()
                self.sparred = True
                answered = True
            elif answer == 8:
                self.compete()
                self.competed = True
                answered = True
            elif answer == 9:
                self.read_notes()
                answered = True
            else:
                print("\nIncorrect input. Let's try again!\n")            

    def eat(self):
        if self.day_part == 1:
            print()
            print("You make yourself an omelet with a side of beef. Delicious!\n")
        elif self.day_part == 2:
            print()
            print("You eat a lite salad with a side of beef. Yum!\n")
        else:
            print()
            print("You eat a good steak with a side of beef. Proteintastic!\n")
        entities.hero.heal_hp(25)
        entities.hero.coins -= 5
        print(f"You healed 25 HP and now have {entities.hero.health} HEALTH total.\n")
        print(f"You spent 5 COINS in ingredients, leaving you with {entities.hero.coins} total.\n")
        print()

    def bath(self):
        if self.day_part == 1:
            print()
            print("You wake up and jump straight into a cold bath. You are the very definition of AWAKE.\n")
        elif self.day_part == 2:
            print()
            print("It's too hot to be outside! Nothing a few ice cubes can't fix...\n")
        else:
            print()
            print("'Nothing like a cold bath to get a good night sleep,' said no one ever.'\n")
        entities.hero.heal_sp(25)
        entities.hero.coins -= 5
        self.bathed = True
        print(f"You healed 25 SP and now have {entities.hero.stamina} STAMINA total.\n")
        print(f"You spent 5 COINS in ice and now have {entities.hero.coins} left.\n")
        print()

    def work(self):
        if self.day_part == 1:
            print()
            print("You deliver newspapers in the morning and come back home to make the best of the day.\n")
        elif self.day_part == 2:
            print()
            print("You brave the heat and go work at a construction site, getting a good sweat in.\n")
        else:
            print()
            print("You finish the day by serving at the local pub.\n")
        coins_gained = 5 * entities.hero.lvl
        entities.hero.coins += coins_gained
        print(f"You gained {coins_gained} COINS, bringing your savings to {entities.hero.coins}.\n")
        time.sleep(2)

    def train(self):
        if self.trained == True and self.bathed == False:
            print()
            print("You try to train but your body fights back. Gotta let it restore itself!\n")
        elif self.trained == True and self.bathed == True:
            print()
            print("WOW! That ice cold bath did the trick! You get in one more workoutl. You found a lifehack!\n")
            xp_gained = 5
            entities.hero.xp += xp_gained
            print(f"You gained {xp_gained} XP, bringing your XP to {entities.hero.xp}.\n")
            time.sleep(2)
        else:    
            if self.day_part == 1:
                print()
                print("You get up and go for a morning job. Can't forget about cardio!\n")
            elif self.day_part == 2:
                print()
                print("You push hard to strengthen your lower body. Never skip leg day!\n")
            else:
                print()
                print("You give your upper body the attention it needs. Arnold ain't got nothing on you!\n")
            xp_gained = 5
            entities.hero.xp += xp_gained
            print(f"You gained {xp_gained} XP, bringing your XP to {entities.hero.xp}.\n")
            time.sleep(2)
    
    def shop(self):
        print("Shop temporarily CLOSED!")
        input("Press ENTER to go back home.")
        print()

    def spar(self):
        enough_cash = False
        self.sparred = False
        while enough_cash == False:
            if entities.hero.coins < 5:
                print("You go to the gym but cannot pay the entry fee. Time for a little work!\n")
                time.sleep(2)
                enough_cash = True
            else:
                entities.hero.coins -= 5        
                print("You go to your local gym to get in a friendly sparring match, \npaying the 5 COIN entry fee as you go in.\n")
                time.sleep(3)
                print("You see Matt and walk over to him.\n")
                print("You don't say a word, as words are not needed.")
                print("This is not Matt's first rodeo.\n")
                print("He is ever ready to go.\n")
                time.sleep(3)
                input("To begin match, press ENTER.\n")
                self.fight.start_fight(entities.hero, entities.matt)
                enough_cash = True
                self.sparred = True
    
    def compete(self):
        if entities.hero.lvl < 3:
            print("WELCOME TO THE FIGHTING ARENA\nwhere champions prove their worth!")
            print()
            print("There are three tiers you can compete in: LOCAL, REGIONAL, and NATIONAL.\nWin all three for a chance to take the World Chamption down!")
            print()
            print("Each champtionship has three fighters you must defeat one after the other.\nAfter each fight, you will have a chance to continue or get out of the competition.")
            print()
            print("Should you make it to the top of tier, special gear will be awarded to you.\nWhat they do is for you to find out!")
            print()
            print("YET TAKE HEED! For fighters here are not your normal sparring partners,\nhaving special abilities to knock you right out.")
            print()
            print("Know also that your chance at fame will not come cheaply, for each tournament comes with a cost.")
            print()
            print("And don't think that we'll just take anyone in! Our sponsors wouldn't like that.")
            print()
            print("So raise your level to LVL 3 and gather 25 COINS to get started, and make sure to write your will before your return.")
            print()
            input("Press ENTER to go back home.")
            print()
        else:
            pass
        
    def read_notes(self):
        print("As you discover more of this world's secrets, they will be added here for your review.")
        print()
        print("A chamption must exercise both mind and body!\n")
        print("Here's a review of what you know so far.")
        print("\n=-•-==-•-==-•-=\nCHARACTER STATS\n=-•-==-•-==-•-=\n")
        print("Your character has three main attributes:")
        print()
        print("ENDURANCE — determined by your HEALTH & STAMINA points, both needed to endure battle.")
        print("STRENGTH - determined by your POWER & DEFENCE skills, used to calculate damage.")
        print("SWIFTNESS - determined by your AGILITY & REFLEXES skills, used to see whether your attacks hit your foe.")
        print()
        print("With each damage taken, your HEALTH is reduced.")
        print("Once it reaches zero, you are knocked out!")
        print()        
        print("With each attack performed, your STAMINA is spent.")
        print("Deplete it completely, and you will be unable to perform an attack!")
        print()
        print("The greater your POWER, the greater the possible damage you deal out.")
        print("The greater your DEFENCE, the greater the possible damage you endure.")
        print()
        print("A higher AGILITY will increase your chances of landing a hit,")
        print("while higher REFLEXES will allow you to more easily evade a blow.")
        print()
        input("Press ENTER to finish reading.")
        print()
