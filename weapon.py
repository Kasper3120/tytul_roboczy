#!/bin/python3
from util import Util
from item import Item


class Weapon(Item):
    """
    String name, Int attack, Int special[chance, dmg/string]
    int crit = crit chance
    """

    def __init__(self, name="", description="", passive={}, attack=0, special=[0, 0], crit=0):
        super().__init__(name, description, passive)
        self.attack = attack
        self.special = special
        self.crit = crit

    def getAttack(self, dice): return round(self.attack*(dice/12))

    def getSpecial(self, dice):
        return self.special[1] if dice > self.special[0] else 0

    def getCrit(self, dice):
        return round(self.attack*1.5) if dice > self.crit else 0

    def __str__(self):
        return f"{self.name}:{self.description}:{self.passive}:{self.attack}:{self.special}:{self.crit}"

    def weaponCreator():
        while True:
            name = input("Set name:\n")
            print("Set attack:")
            attack = Util.parseInt()
            print("Set crit chance:")
            crit_chance = Util.parseInt()
            print("Set special chance:")
            spec_chance = Util.parseInt()
            print("Set special damage:")
            special_dmg = Util.parseInt()
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
                    Util.saveWeapon(weapon)
                    return
                elif choice == 'n':
                    break
                elif choice == "0":
                    return


def main():
    Weapon.weaponCreator()


if __name__ == '__main__':
    main()
