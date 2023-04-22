#!/bin/python3
from util import Util

class Weapon:
    """
    String name, Int attack, Int special[chance, dmg/string]
    int crit = crit chance
    """
    def __init__(self, name, attack, special, crit):
        self.name = name
        self.attack = attack
        self.special = special
        self.crit = crit

    def getAttack(self, dice):
        return round(self.attack*(dice/12))

    def getSpecial(self, dice):
        return self.special[1] if dice > self.special[0] else 0

    def getCrit(self, dice):
        return round(self.attack*1.5) if dice > self.crit else 0

    def __str__(self):
        return f"{self.name}:{self.attack}:{self.special}:{self.crit}"

    def getName(self): return self.name

    def weaponCreator():
        while True:
            name = input("Set name")
            print("Set attack")
            attack = Util.parseInt()
            print("Set crit chance")
            crit_chance = Util.parseInt()
            print("Set special chance")
            spec_chance = Util.parseInt()
            print("Set special damage")
            special_dmg = Util.parseInt()
            weapon = Weapon(
                    name,
                    attack,
                    [spec_chance, special_dmg],
                    crit_chance
                    )
            print(weapon)
            while True:
                print("Save weapon? (y/n-try again/0-exit)")
                choice = input()
                if choice == 'y':
                    Util.saveWeapon(weapon)
                    return
                elif choice == 'n':
                    break
                elif choice == "0":
                    return
