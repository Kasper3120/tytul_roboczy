#!/bin/python3

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
