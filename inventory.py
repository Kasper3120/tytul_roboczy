#!/bin/python3

class Inventory:
    def __init__(self, weapon, armor=0, backpack={}):
        self.weapon = weapon
        self.armor = armor
        self.backpack = backpack

    def __str__(self):
        return f"w:({self.weapon})a:{self.armor}b:{self.backpack}"

    def getArmor(self): return self.armor
