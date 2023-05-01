#!/bin/python3

from weapon import Weapon
from inventory import Inventory
from util import Util

import pdb


class Character:
    def __init__(self, name, hp,
                 inventory=Inventory(Weapon("hands", 2, [6, 1], 8), 0, {}),
                 strength=0, agility=0, status=[]):
        self.name = name
        self.hp = hp
        self.inventory = inventory
        self.strength = strength
        self.agility = agility
        self.status = status

    def attack(self, who, attack_dice, crit_dice):
        # TODO: bug - if no armor function throws an exception
        attack = self.inventory.weapon.getAttack(attack_dice) - who.inventory.getArmor()
        crit_attack = self.inventory.weapon.getCrit(crit_dice) - who.inventory.getArmor()

        if crit_attack > 0:
            who.hp -= crit_attack
            print(f"{self.name} attacks criticaly {who.name} for {crit_attack} hp")
        elif attack > 0:
            who.hp -= attack
            print(f"{self.name} attacks {who.name} for {attack} hp")
        else:
            print(f"{self.name}'s attack ({attack}) didn't penetrate {who.name}'s armor")

    def special(self, weapon, who, special_dice): pass

    def isDead(self): return self.hp <= 0

    def getName(self): return self.name

    def setName(self, name): self.name = name

    def getHp(self): return self.hp

    def __str__(self):
        return f"name:{self.name};hp:{self.hp};inv:{self.inventory}"


def characterCreator():
    while True:
        name = input("Set name\n")
        print("Set hp")
        hp = Util.parseInt()
        print("Set strength")
        strength = Util.parseInt()
        print("Set agility")
        agility = Util.parseInt()
        # TODO: status
        print("Set Armor")
        armor = Util.parseInt()
        print("Set Weapon")
        pdb.set_trace()
        weapon = Util.weaponSearch()
        character = Character(name, hp, Inventory(weapon, armor, {}), strength, agility)
        while True:
            print(character)
            print("Save character? (y/n-try again/0-exit)")
            choice = input()
            if choice == 'y':
                Util.saveCharacter(character)
                return
            elif choice == 'n':
                break
            elif choice == "0":
                return


def main():
    print("Welcome to character creator!")
    while True:
        print("Do you want to create new character (y/n)")
        choice = input()
        if choice == 'y':
            characterCreator()
            return
        elif choice == 'n':
            return
        else:
            print("Wrong input")


if __name__ == "__main__":
    main()
