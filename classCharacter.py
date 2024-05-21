#create dictionaries for characters with values that change as user interacts

import random
import time

from tools import slow_print

class Character:
    def __init__(self, name, health, max_health, stamina, max_stamina, power, defence, agility, reflexes, xp, coins, crowd, never, berserk, rank):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.stamina = health
        self.max_stamina = max_stamina
        self.power = power
        self.defence = defence
        self.agility = agility
        self.reflexes = reflexes
        self.xp = xp
        self.coins = coins
        self.crowd = crowd
        self.never = never
        self.berk = berserk
        self.rank = rank
        
    def is_alive(self):
        return self.health > 0
    
    def punch(self, enemy):
        if not self.is_alive():
            return
        print(f"{self.name} tries to punch {enemy.name}...\n")
        time.sleep(1)
        if self.stamina < 5:
            print(f"{self.name} is worn out and stumbles to the ground!")
        else:
            if enemy.avoid_attack(self) == True:
                print(f"{self.name} misses!\n")
            else:
                probability_threshold = 0.25
                if random.random() < probability_threshold:
                    print(f"{self.name} lands a MASSIVE blow!")
                    damage_given = (random.randint(int(int(self.power) / 3), int(self.power))) - random.randint(1, int(enemy.defence / 2)) * 1.5
                    if damage_given < (int(self.power) / 2):
                        damage_given = int(int(self.power) / 2)
                    damage_given = int(damage_given)
                    print(f"{self.name} deals {damage_given} damage.\n")
                    enemy.receive_damage(damage_given)

                else:
                    print(f"{self.name} lands a regular blow!")
                    damage_given = random.randint(1, int(int(self.power) / 3)) - random.randint(1, int(int(enemy.defence) / 2))
                    damage_given = int(damage_given)
                    if damage_given < (int(self.power) / 2):
                        damage_given = int(int(self.power) / 2)
                    print(f"{self.name} deals {damage_given} damage.\n")
                    enemy.receive_damage(damage_given)
        self.stamina -= 5
        if self.stamina < 0:
            self.stamina = 0
        time.sleep(1)
            
    def kick(self, enemy):
        if not self.is_alive():
            return
        print(f"{self.name} tries to kick {enemy.name}...\n")
        time.sleep(1)
        if self.stamina < 10:
            print(f"{self.name} is worn out and stumbles to the ground!")
        else:
            if enemy.avoid_attack(self) == True:
                print(f"{self.name} misses!\n")
            else:
                probability_threshold = 0.50
                if random.random() < probability_threshold:
                    print(f"{self.name} lands a MASSIVE kick!")
                    damage_given = (random.randint(int(int(self.power) / 2), int(self.power))) - random.randint(1, int(int(enemy.defence) / 2)) * 2
                    damage_given = int(damage_given)
                    if damage_given < (int(self.power) / 2):
                        damage_given = int(int(self.power) / 2)
                    damage_given = int(damage_given)
                    print(f"{self.name} deals {damage_given} damage.\n")
                    enemy.receive_damage(damage_given)
                else:
                    print(f"{self.name} lands a regular kick!")
                    damage_given = (random.randint(1, int(int(self.power) / 2)) - random.randint(1, int(int(enemy.defence) / 2)))
                    damage_given = int(damage_given)
                    if damage_given < (int(self.power) / 2):
                        damage_given = int(int(self.power) / 2)
                    print(f"{self.name} deals {damage_given} damage.\n")
                    enemy.receive_damage(damage_given)
        self.stamina -= 10
        if self.stamina < 0:
            self.stamina = 0
        time.sleep(1)

    def avoid_attack(self, enemy):
        if random.randint(1, int(self.reflexes)) - random.randint(1, int(enemy.agility)) > 0:
            return True
        
    def receive_damage(self, points):
        self.health -= points
        if self.health < 0:
            self.health = 0
            
    def is_knockout(self, hero):
        print(f"You are victorious! You gain {self.xp} XP and {self.coins} COINS.\n")
        hero.xp += self.xp
        return hero.xp
        hero.coins += self.coins
        return hero.coins
    
    def heal_hp(self, points):
        self.health += points
        if self.health > self.max_health:
            self.health = self.max_health
            return self.health
        return self.health
    
    def heal_sp(self, points):
        self.stamina += points
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
        return self.stamina
        
    def print_status(self):
        print(f"{self.name} currently has {self.health} of {self.max_health} HEALTH POINTS and {self.stamina} of {self.max_stamina} STAMINA POINTS with the following stats:\n\n * POWER: {self.power} • DEFENCE: {self.defence}\n * AGILITY: {self.agility} • REFLEXES: {self.reflexes}\n")
        
    def do_crowd_favorite(self):
        if self.rank == 1:
            self.stamina += 0.05 * self.stamina
        elif self.rank == 2:
            self.stamina += 0.10 * self.stamina
        elif self.rank == 3:
            self.stamina += 0.15 * self.stamina
            
    def do_berserker(self):
        if self.rank == 1:
            self.stamina += 0.05 * self.stamina
        elif self.rank == 2:
            self.stamina += 0.10 * self.stamina
        elif self.rank == 3:
            self.stamina += 0.15 * self.stamina
            
    def do_never_give_up(self):
        if self.rank == 1:
            self.stamina += 0.05 * self.stamina
        elif self.rank == 2:
            self.stamina += 0.10 * self.stamina
        elif self.rank == 3:
            self.stamina += 0.15 * self.stamina

            
class Hero(Character):
    def __init__(self, name, health, max_health, stamina, max_stamina, power, defence, agility, reflexes, xp, coins, crowd, never, berserk, rank, lvl, lvl_2, lvl_3, lvl_4, lvl_5, lvl_6, lvl_7, lvl_8, lvl_9, lvl_10, lvl_11, lvl_12):
        super().__init__(name, health, max_health, stamina, max_stamina, power, defence, agility, reflexes, xp, coins, crowd, never, berserk, rank)
        self.lvl = lvl
        self.items = []
        self.gear = []
        self.power = power
        self.lvl_2 = lvl_2
        self.lvl_3 = lvl_3
        self.lvl_4 = lvl_4
        self.lvl_5 = lvl_5
        self.lvl_6 = lvl_6
        self.lvl_7 = lvl_7
        self.lvl_8 = lvl_8
        self.lvl_9 = lvl_9
        self.lvl_10 = lvl_10
        self.lvl_11 = lvl_11
        self.lvl_12 = lvl_12
        
    def lvl_evolution(self):
        if self.lvl == 1 and self.xp >= self.lvl_2:
            print("CONGRATULATIONS!\nYou reached Level 2!")
            self.add_stats()
        elif self.lvl == 2 and self.xp >= self.lvl_3:
            print("CONGRATULATIONS!\nYou reached Level 3!")
            self.add_stats()
        elif self.lvl == 3 and self.xp >= self.lvl_4:
            print("CONGRATULATIONS!\nYou reached Level 4!")
            self.add_stats()   
        elif self.lvl == 4 and self.xp >= self.lvl_5:
            print("CONGRATULATIONS!\nYou reached Level 5!")
            self.add_stats()
        elif self.lvl == 5 and self.xp >= self.lvl_6:
            print("CONGRATULATIONS!\nYou reached Level 6!")
            self.add_stats()
        elif self.lvl == 6 and self.xp >= self.lvl_7:
            print("CONGRATULATIONS!\nYou reached Level 7!")
            self.add_stats()
        elif self.lvl == 7 and self.xp >= self.lvl_8:
            print("CONGRATULATIONS!\nYou reached Level 8!")
            self.add_stats()
        elif self.lvl == 8 and self.xp >= self.lvl_9:
            print("CONGRATULATIONS!\nYou reached Level 9!")
            self.add_stats()
        elif self.lvl == 9 and self.xp >= self.lvl_10:
            print("CONGRATULATIONS!\nYou reached Level 10!")
            self.add_stats()

    def add_stats(self):
        self.lvl += 1
        endurance_question_answered = False
        skill_question_answered = False
        while endurance_question_answered == False:
            print("You have 10 additional ENDURANCE POINTS to spread between HEALTH & STAMINA.\n")
            add_health = int(input("How many do you want for HEALTH?\n> "))
            add_stamina = int(input("How many do you want for STAMINA?\n> "))
            if add_health + add_stamina > 10:
                print("That's more than 10! Let's try again.")
                print()
                endurance_question_answered = False
            elif add_health + add_stamina < 10:
                print("That's less than 10! Let's try again.")
                print()
                endurance_question_answered = False
            else:
                redo_endurance = input(f"\nYou have chosen:\n\n * {add_health} for HEALTH\n * {add_stamina} for STAMINA\n\n1 — REDO\n2 — ACCEPT!\n> ")
                if redo_endurance == "1":
                    endurance_question_answered = False
                elif redo_endurance == "2":
                    endurance_question_answered = True
                else:
                    print("That is an incorrent entry. Let's try again!\n")
                    endurance_question_answered = False
                    
        self.max_health += add_health
        self.health = self.max_health
        self.max_stamina += add_stamina
        self.stamina = self.max_stamina

        print(f"\nYour MAX HP rises to {self.max_health} and your MAX SP to {self.max_stamina}.\nYou also FULLY HEAL!")
        time.sleep(3)
        print("Now let's move on to your SKILLS...")
        time.sleep(2)
        print("\nYou have 4 POINTS available to spread among: \n\n * POWER & DEFENCE for your overall STRENGTH, \n * AGILITY & REFLEXES for your overall SWIFTNESS.")
        print()
        
        while skill_question_answered == False:
            add_power = int(input("How many do you want for POWER?\n> "))
            add_defence = int(input("How many do you want for DEFENCE?\n> "))
            add_agility = int(input("How many do you want for AGILITY?\n> "))
            add_reflexes = int(input("How many do you want for REFLEXES?\n> "))

            if add_power + add_defence + add_agility + add_reflexes > 4:
                print("\nThat's more than 4! Let's try again.")
                print()
                skill_question_answered = False
            elif add_power + add_defence + add_agility + add_reflexes < 4:
                print("\nThat's less than 4! Let's try again.")
                print()
                skill_question_answered = False
            else:
                redo_skills = input(f"\nYou have chosen:\n\n * {add_power} for POWER,\n * {add_defence} for DEFENCE, \n * {add_agility} for AGILITY,\n * {add_reflexes} for REFLEXES.\n\n1 — REDO\n2 — ACCEPT!\n> ")
                if redo_skills == "1":
                    skill_question_answered = False
                elif redo_skills == "2":
                    skill_question_answered = True
                else:
                    print("That is an incorrent entry. Let's try again!\n")
                    skill_question_answered = False
         
        self.power = int(self.power) + int(add_power)
        self.defence = int(self.defence) + int(add_defence)
        self.agility += int(self.agility) + int(add_agility)
        self.reflexes += int(self.reflexes) + int(add_reflexes)
        
        print("\nCONGRATULATIONS! \n\nHere are your upgraded stats:")
        time.sleep(2)
        print()
        print(f" * MAX HEALTH: {self.max_health}")
        print(f" * MAX STAMINA: {self.max_stamina}")
        print(f" * POWER: {self.power}")
        print(f" * DEFENCE: {self.defence}")
        print(f" * AGILITY: {self.agility}")
        print(f" * REFLEXES: {self.reflexes}")
        time.sleep(2)

    def do_guard(self):
        health_up = random.randint(int(int(self.defence) / 2), self.defence)
        self.health += health_up
        if self.health > self.max_health:
            self.health = self.max_health
        stamina_up = random.randint(int(int(self.reflexes) / 2), self.reflexes)
        self.stamina += stamina_up
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
        print(f"{self.name} guarded and healed {health_up} HP and recovered {stamina_up} SP!\n")
            
    def use_item(self, item):
        item.apply(hero)
    
class Opponent(Character):
    def __init__(self, name, health, max_health, stamina, max_stamina, power, defence, agility, reflexes, xp, coins, crowd, never, berserk, rank):
        super().__init__(name, health, max_health, stamina, max_stamina, power, defence, agility, reflexes, xp, coins, crowd, never, berserk, rank)
        
 