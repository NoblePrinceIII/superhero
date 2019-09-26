import random


# Super Hero's Ability
class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        strongest_attack = random.randint(0, self.attack_strength)
        return strongest_attack


# Super Hero's Armor
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        block = random.randint(0, self.max_block)
        return block


class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armor = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        damage_total = 0
        for ability in self.abilities:
            damage_total += ability.attack()
        return damage_total

    def defend(self):
    # adds "block" on each armor
        block_total = 0
        for armor in self.armor:
            block_total += armor.block()

        return block_total


    def add_armor(self, armor):
    # Calculates the total damage from all ability attacks
        self.armor.append(armor)

    def take_damage(self, damage):
    # Adds armor object which is passed in self.armors
        self.current_health -= damage - self.defend()

    def is_alive(self):
        if self.current_health >= 0:
            return True
        else:
            return False


    def fight(self):
        pass



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
