#!/bin/python3
from util import parseInt, saveWeapon
from item import Item

from typing import List


class Weapon(Item):
    def __init__(self, name: str = "", description: str = "", passive: dir = {}, attack: int = 0, special: List[int] = [0, 0], crit: int = 0):
        """
        String name, Int attack, Int special[chance, dmg/string]
        int crit = crit chance
        """
        super().__init__(name, description, passive)
        self.attack = attack
        self.special = special
        self.crit = crit

    def getAttack(self, dice: int) -> float: return round(self.attack*(dice/12))

    def getSpecial(self, dice: int) -> int or str:
        return self.special[1] if dice > self.special[0] else 0

    def getCrit(self, dice: int) -> float:
        return round(self.attack*1.5) if dice > self.crit else 0

    def __str__(self) -> str:
        return f"{self.name}:{self.description}:{self.passive}:{self.attack}:{self.special}:{self.crit}"

    def weaponCreator() -> None:
        while True:
            name = input("Set name:\n")
            print("Set attack:")
            attack = parseInt()
            print("Set crit chance:")
            crit_chance = parseInt()
            print("Set special chance:")
            spec_chance = parseInt()
            print("Set special damage:")
            special_dmg = parseInt()
            weapon = Weapon(
                    name,
                    attack,
                    [spec_chance, special_dmg],
                    crit_chance
                    )
            while True:
                print(weapon)
                print("Save weapon? (y/n-try again/0-exit)")
                choice = input()
                if choice == 'y':
                    saveWeapon(weapon)
                    return
                elif choice == 'n':
                    break
                elif choice == "0":
                    return


def main():
    Weapon.weaponCreator()


if __name__ == '__main__':
    main()
