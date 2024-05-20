class Item:
    def __init__(self, name, cost, health_effect, stamina_effect, power_effect, defense_effect, agility_effect, reflexes_effect, duration):
        self.name = name
        self.cost = cost
        self.health_effect = health_effect
        self.stamina_effect = health_stamina
        self.power = power
        self.defense = defense
        self.agility = agility
        self.reflexes = reflexes
        self.duration = duration
        
    def hp_up(self, character):
        character.health += health_effect
        print(f"{character.name}'s health healed by {self.health_effect}, raising it to {character.health}.")
    
    def stamina_up(self, character):
        character.stamina += stamina_effect
        print(f"{character.name}'s stamina replenished by {self.health_effect}, raising it to {character.health}.")
    
    def strength_up(self, character):
        pass
    
    def swiftness_up(self, character):
        pass