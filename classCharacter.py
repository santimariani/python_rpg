import random
import time

from tools import slow_print
from classLevel import Level

class Character:
    def __init__(self, name, health, max_health, stamina, max_stamina, power, defense, agility, reflexes, xp, coins, crowd, never, berserk, rank):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.stamina = health
        self.max_stamina = max_stamina
        self.power = power
        self.defense = defense
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
        time.sleep(2)
        if enemy.avoid_attack(self) == True:
            print(f"{self.name} misses!\n")
        else:
            probability_threshold = 0.25
            if random.random() < probability_threshold:
                print(f"{self.name} lands a MASSIVE blow!")
                damage_given = (random.randint(int(self.power/2), self.power) * 1.50) - random.randint(1, enemy.defense)
                damage_given = int(damage_given)
                if damage_given < 1:
                    damage_given = 1
                print(f"{self.name} deals {damage_given} damage.\n")
                enemy.receive_damage(damage_given)

            else:
                print(f"{self.name} lands a regular blow!")
                damage_given = (random.randint(1, self.power) - random.randint(1, enemy.defense))
                damage_given = int(damage_given)
                if damage_given < 1:
                    damage_given = 1
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
        time.sleep(2)
        if enemy.avoid_attack(self) == True:
            print(f"{self.name} misses!\n")
        else:
            probability_threshold = 0.50
            if random.random() < probability_threshold:
                print(f"{self.name} lands a MASSIVE kick!")
                damage_given = (random.randint(int(self.power/2), self.power) * 2) - random.randint(1, enemy.defense)
                if damage_given < 1:
                    damage_given = 1
                damage_given = int(damage_given)
                print(f"{self.name} deals {damage_given} damage.\n")
                enemy.receive_damage(damage_given)
            else:
                print(f"{self.name} lands a regular kick!")
                damage_given = (random.randint(1, self.power) - random.randint(1, enemy.defense))
                damage_given = int(damage_given)
                if damage_given < 1:
                    damage_given = 1
                print(f"{self.name} deals {damage_given} damage.\n")
                enemy.receive_damage(damage_given)
        self.stamina -= 10
        if self.stamina < 0:
            self.stamina = 0
        time.sleep(1)
        
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
        
    def avoid_attack(self, enemy):
        if random.randint(1, self.reflexes) - random.randint(1, enemy.agility) > 0:
            return True
    
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
        print(f"{self.name} currently has {self.health} of {self.max_health} HEALTH POINTS and {self.stamina} of {self.max_stamina} STAMINA POINTS with the following stats:\n\n * POWER: {self.power} • DEFENSE: {self.defense}\n * AGILITY: {self.agility} • REFLEXES: {self.reflexes}\n")
        
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
    def __init__(self, name, health, max_health, stamina, max_stamina, power, defense, agility, reflexes, xp, coins, crowd, never, berserk, rank, lvl, lvl_2, lvl_3, lvl_4, lvl_5, lvl_6, lvl_7, lvl_8, lvl_9, lvl_10, lvl_11, lvl_12):
        super().__init__(name, health, max_health, stamina, max_stamina, power, defense, agility, reflexes, xp, coins, crowd, never, berserk, rank)
        self.lvl = lvl
        self.items = []
        self.gear = []
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
        self.level = Level()
    
    def lvl_evolution(self):
        if self.lvl == 1 and self.xp >= self.lvl_2:
            print("You reached Level 2!")
            self.level.add_stats()
        elif self.lvl == 2 and self.xp >= self.lvl_3:
            print("You reached Level 3!")
            self.level.add_stats()
        elif self.lvl == 3 and self.xp >= self.lvl_4:
            print("You reached Level 4!")
            self.level.add_stats()   
        elif self.lvl == 4 and self.xp >= self.lvl_5:
            print("You reached Level 5!")
            self.level.add_stats()
        elif self.lvl == 5 and self.xp >= self.lvl_6:
            print("You reached Level 6!")
            self.level.add_stats()
        elif self.lvl == 6 and self.xp >= self.lvl_7:
            print("You reached Level 7!")
            self.level.add_stats()
        elif self.lvl == 7 and self.xp >= self.lvl_8:
            print("You reached Level 8!")
            self.level.add_stats()
        elif self.lvl == 8 and self.xp >= self.lvl_9:
            print("You reached Level 9!")
            self.level.add_stats()
        elif self.lvl == 9 and self.xp >= self.lvl_10:
            print("You reached Level 10!")
            self.level.add_stats()
            
    def do_guard(self):
        health_up = random.randint(1, self.defense)
        self.health += health_up
        if self.health > self.max_health:
            self.health = self.max_health
        stamina_up = random.randint(1, self.reflexes)
        self.stamina += stamina_up
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
        print(f"{self.name} guarded and healed {health_up}HP and recovered {stamina_up}SP!\n")
            
    def use_item(self, item):
        item.apply(hero)
    
class Opponent(Character):
    def __init__(self, name, health, max_health, stamina, max_stamina, power, defense, agility, reflexes, xp, coins, crowd, never, berserk, rank):
        super().__init__(name, health, max_health, stamina, max_stamina, power, defense, agility, reflexes, xp, coins, crowd, never, berserk, rank)
    
