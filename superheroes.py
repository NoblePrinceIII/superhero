import random


class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # """Return a value between 0 and the value set by self.max_damage."""
        strongest_attack = random.randint(0, self.attack_strength)
        return strongest_attack



class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        block = random.randint(0, self.max_block)
        return block



class Weapon(Ability):
    def attack(self):
        half_strength = self.attack_strength // 2
        return random.randint(half_strength, self.attack_strength)



class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armor = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0
    def add_ability(self, ability):
    # """ability object to abilities:List"""
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abiilities.append(weapon)



    def attack(self):
        damage_total = 0
        for ability in self.abilities:
            damage_total += ability.attack()
        return damage_total

    def defend(self, damage_amt):
    # """ adds "block" on each armor"""
        damage_amt = 0
        for armor in self.armor:
            damage_amt += armor.block()
        return block_total

    def add_armor(self, amor):
    # """Calculates the total damage from all ability attacks"""
        self.armor.append(armor)

    def take_damage(self, damage):
 # """Updates self.current_health to reflect the damage minus the defense."""
        self.current_health -= damage - self.defend()


    def is_alive(self):
        if self.current_health >= 0:
            return True
        else:
            return False

    def add_kill(self, num_kills):
        # This method should add the number of kills to self.kills
        self.kills += num_kills
        return self.kills

    def add_deaths(self, num_deaths):
        # This method should add the number of deaths to self.deaths
        self.deaths += num_deaths
        return self.deaths

    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            return print("Draw")
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            if self.is_alive() == False:
                self.add_deaths(1)
                opponent.add_kill(1)
                return print(f"{opponent.name} won!")

            else:
                self.add_kill(1)
                opponent.add_deaths(1)
                return print(f"{self.name} won!")




class Team:
    # Initialize Team
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    # remove hero from list
    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def attack(self, other_team):
        hero = random.choice(self.heroes)
        opponenet = random.choice(other_team.heroes)
        Hero.fight(hero, opponent)

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        for hero in self.heroes:
            print(hero.name, hero.kills, hero.deaths, hero.abilities, hero.armor)



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 90)
    ability2 = Ability("Super Eyes", 80)
    ability3 = Ability("Wizard Wand", 11000)
    ability4 = Ability("Wizard Beard", 10000)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
