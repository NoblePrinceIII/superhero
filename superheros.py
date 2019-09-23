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


# class Hero:
#     def __init__(self, name, starting_health):
#         self.name = name
#         self.starting_health = starting_health
#
#     def add_ability(self, ability):
#         self.ability = ability
#
#     # def attack():
#     # def defend():
#
#     def take_damage(self, damage):
#         self.damage = damage
#
#     # def is_alive():
#
#
#     def fight(self, opponent):
#         self.opponent = opponent


if __name__ == "__main__"
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
