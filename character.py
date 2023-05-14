#!/bin/python3

from weapon import Weapon
from inventory import Inventory
from item import Item
from util import parseInt, weaponSearch, saveCharacter
# from character import Character

import pdb


class Character:
    def __init__(self, name: str, hp: int,
                 inventory: Inventory = Inventory(Weapon("hands", 2, [6, 1], 8), 0, {}),
                 strength: int = 0, agility: int = 0, status: list = []):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.inventory = inventory
        self.strength = strength
        self.agility = agility
        self.status = status

    def attack(self, who, attack_dice: int, crit_dice: int):
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

    def chooseItem(self) -> bool:
        for i, item in enumerate(self.inventory.backpack):
            print(f"{i}. {item.name}")
        print(f"{len(self.inventory.backpack)}. Return to menu.")
        chosen_item = parseInt()
        if chosen_item == len(self.inventory.backpack):
            return False
        elif chosen_item < 0 or chosen_item >= len(self.inventory.backpack):
            print("Wrong item number")
        else:
            self.inventory.backpack[chosen_item].consume(self)
            print(f"{self.inventory.backpack[chosen_item].name} got consumed")
            self.inventory.backpack.pop(chosen_item)
            return True
            # TODO: exclude not consumable
            # TODO: uniq + count

    # TODO: add tests for that
    def executeStatus(self) -> None:
        pdb.set_trace()
        for status_name, status_numbers in self.status:
            status_numbers[0] -= 1
            if status_name in ("heal", "bleeding", "poisoning", "hurt"):
                if status_name == "heal":
                    self.hp += status_numbers[1]
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                else:
                    self.hp -= status_numbers[1]
                if status_numbers[0] == 0:
                    # del self.status[[status_name, status_numbers]]
                    self.status.remove([status_name, status_numbers])
            if status_name == "strength":
                # TODO: think about that :)
                pass
            if status_name == "agility":
                pass

    def special(self, weapon, who, special_dice): pass

    def isDead(self) -> bool: return self.hp <= 0

    def getName(self) -> str: return self.name

    def setName(self, name: str) -> None: self.name = name

    def getHp(self) -> int: return self.hp

    def pickUpItem(self, item: Item) -> None: self.inventory.backpack.append(item)

    def __str__(self) -> str:
        return f"name:{self.name};hp:{self.hp};inv:{self.inventory}"


def characterCreator() -> None:
    while True:
        name = input("Set name\n")
        print("Set hp")
        hp = parseInt()
        print("Set strength")
        strength = parseInt()
        print("Set agility")
        agility = parseInt()
        print("Set Armor")
        armor = parseInt()
        print("Set Weapon")
        weapon = weaponSearch()
        character = Character(name, hp, Inventory(weapon, armor, {}), strength, agility)
        while True:
            print(character)
            print("Save character? (y/n-try again/0-exit)")
            choice = input()
            if choice == 'y':
                saveCharacter(character)
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
