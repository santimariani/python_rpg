import entities

class Level:
    def __init__(self):
        self.name = True
        
    def add_stats(self):
        entities.hero.lvl =+ 1
        endurance_question_answered = True
        skill_guestion_answered = True
        while first_question_answered == False:
            answer_endurance = input("You have 10 additional endurance points. How would you like to use it?\n\n1—Increase Health\n2—Increase Stamina\n")
            if answer_endurance == 1:
                entities.hero.health += 10
                print("Your endurance grows! Your health is now {hero.health}")
                endurance_question_answered == True
            elif answer_endurance == 2:
                entities.hero.stamina += 10
                print("Your endurance grows! Your stamina is now {hero.stamina)")
                endurance_question_answered == True
            else:
                print("... sayeth what? Try agian!")
                continue
        while skill_question_answered == False:
            answer_skill = input("You have 1 additional skill points. How would you like to use it?\n\n1—Increase Power\n2—Increase Defense\n3-Increase Agility\n4-Increase Reflexes\n")
            if answer_skill == 1:
                entities.hero.power += 1
                print("Your skill grows! Your power is now {hero.power}")
                skill_question_answered == True
            elif answer_skill == 2:
                entities.hero.defense += 1
                print("Your skill grows! Your defense is now {hero.defense)")
                skill_question_answered == True
            elif answer_skill == 3:
                entities.hero.agility += 1
                print("Your skill grows! Your agility is now {hero.agility}")
                skill_question_answered == True
            elif answer_skill == 4:
                entities.hero.reflexes += 1
                print("Your skill grows! Your reflexes are now {hero.reflexes)")
                skill_question_answered == True
            else:
                print("... sayeth what? Try agian!")
                continue   