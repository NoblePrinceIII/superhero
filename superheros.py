import random


# Super Hero's Ability
class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        strongest_attack = random.randint(self.attack_strength, 100)
        return strongest_attack


# Super Hero's Armor
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self, max_block):
        block = random.randitI(self.max_block, 100)
pass


class Hero:
    def __init__(self, name, current_health, starting_health):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = current_health

    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        pass
    def defend(self):
        pass
    def take_damage(self, damage):
        pass
    def is_alive(self):
        pass
    def fight(self):
        pass



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200, 200)
    hero.add_ability(ability)
    print(hero.abilities)
