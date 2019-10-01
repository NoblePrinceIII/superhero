import random


class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # Return a value between 0 and the value set by self.max_damage
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
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        # adds abilitiy to abilities list
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        # adds weapon to abilities list
        self.abilities.append(weapon)

    def attack(self):
        damage_total = 0
        for a in self.abilities:
            damage_total += a.attack()
        return damage_total

    def defend(self):
        # adds "block" on each armor
        damage_amt = 0
        for armor in self.armors:
            damage_amt += armor.block()
        return damage_amt

    def add_armor(self, armor):
        # Calculates the total damage from all ability attacks
        a = Armor(armor.name, armor.max_block)
        self.armors.append(a)

    def take_damage(self, damage):
        # Updates self.current_health to reflect the damage minus the defense.
        self.current_health -= damage - self.defend()

    def is_alive(self):
        # checks if Hero is alive
        if self.current_health > 0:
            return True
        else:
            return False

    def add_kill(self, num_kills):
        # adds the amount of kills to self.kills
        self.kills += num_kills
        return self.kills

    def add_deaths(self, num_deaths):
        # adds the amount of deaths to self.deaths
        self.deaths += num_deaths
        return self.deaths

    def fight(self, opponent):
        # checks if oppoenent wins lose or draw also adds death and kill count
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        if self.is_alive() is False:
            self.add_deaths(1)
            opponent.add_kill(1)
            print(f"{opponent.name} won!")
        elif opponent.is_alive() is False:
            self.add_kill(1)
            opponent.add_deaths(1)
            print(f"{self.name} won!")

class Team:
    def __init__(self, name):
        # Initialize Team
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        # remove hero from list
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return
        return 0

    def view_all_heroes(self):
        # Prints Hero names
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        # adds hero to self.heroes list
        self.heroes.append(hero)

    def attack(self, other_team):
        # Randomly select a living hero from each team and have
        while len(self.living_heroes()) > 0 and len(other_team.living_heroes()) > 0:
            hero_1 = random.choice(self.living_heroes())
            hero_2 = random.choice(other_team.living_heroes())
            hero_1.fight(hero_2)

    def living_heroes(self):
        living_hero = []
        for hero in self.heroes:
            if hero.is_alive() is True:
                living_hero.append(hero)
        return living_hero

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        for hero in self.heroes:
            print(f"{hero.name}'s K/D/R: {hero.kills}/{hero.deaths}")


class Arena:
    def __init__(self):
        self.team_one = Team("team one")
        self.team_two = Team("team two")

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input'''
        user_ability_name = input("Enter your Abilitiy Here: ")
        user_ability_attack_strength = int(input("Enter Number Value for Attack Strength Here: "))
        return Ability(user_ability_name, user_ability_attack_strength)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.'''
        user_weapon_name = input("Enter Weapon Name Here: ")
        user_weapon_attack_strength = int(input("Enter Number Value for Weapon Attack Strength Here: "))
        return Weapon(user_weapon_name, user_weapon_attack_strength)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.'''
        user_armor_name = input("Enter Armor Here: ")
        user_armor_max_block = int(input("Enter a Value for Armor Block Strength Here: "))
        return Armor(user_armor_name, user_armor_max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.'''
        superhero_name = input("Hero name: ")
        new_hero = Hero(superhero_name)
        abilities = self.create_ability()
        armors = self.create_armor()
        weapons = self.create_weapon()
        new_hero.add_ability(abilities)
        new_hero.add_armor(armors)
        new_hero.add_weapon(weapons)
        return Hero(superhero_name)

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        first_team_heroes = int(input(f"select amount of heroes on {self.team_one.name}: "))
        for i in range(first_team_heroes):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        second_team_heroes = int(input(f"select amount of heroes on {self.team_two.name}: "))
        for j in range(second_team_heroes):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("The Results are: ")
        self.team_one.stats()
        self.team_two.stats()


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()
    game_is_running = True
    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
