#!/bin/python3


class Inventory:
    def __init__(self, weapon, armor: int = 0, backpack: list = []):
        self.weapon = weapon
        self.armor = armor
        self.backpack = backpack

    def __str__(self) -> str:
        return f"w:({self.weapon}):a:{self.armor}:b:{self.backpack}"

    def getArmor(self) -> int:
        if self.armor:
            return self.armor
        else:
            print("no armor")
            return 0
