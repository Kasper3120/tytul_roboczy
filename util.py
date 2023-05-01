#!/bin/python3
# from character import Character

from random import randrange
from os import listdir
import pickle


class Util:
    def roll(times=1):
        output = 0
        for i in range(0, times):
            output += randrange(1, 7)
        return output

    def parseInt():
        while True:
            str = input()
            try:
                return int(str)
            except ValueError:
                print("Pass a number")

    def testAttack(self, who, times=10, armor=0):
        pass
        # TODO: change func accordingly to current fight interface
        # for i in range(0, times):
        #     who.attack(
        #             who.inventory.weapon,
        #             Character("dummy", 0, {"armor": armor}),
        #             self.roll(2),
        #             self.roll(2),
        #         )

    def saveCharacter(character):
        with open(f'./bin/characters/{character.getName()}.dat', 'wb') as f:
            pickle.dump(character, f)

    def loadCharacter(name):
        with open(f'./bin/characters/{name}.dat', 'rb') as f:
            return pickle.load(f)

    def saveWeapon(weapon):
        with open(f'./bin/weapons/{weapon.getName()}.dat', 'wb') as f:
            pickle.dump(weapon, f)

    def loadWeapon(name):
        with open(f'./bin/weapons/{name}.dat', 'rb') as f:
            return pickle.load(f)

    def weaponSearch():
        list = listdir("./bin/weapons/")
        while True:
            weapon = input()
            if weapon == "0":
                return
            if weapon+".dat" in list:
                return Util.loadWeapon(weapon)
            else:
                print("No such weapon in database, try another name; type 0 to exit")

    def updateCharacter(name, what, to):
        character = Util.loadCharacter(name)
        if what == "name":
            character.name = to
        if what == "hp":
            character.hp = to
        if what == "strength":
            character.strength = to
        if what == "agility":
            character.agility = to
        if what == "status":
            character.status = to
        if what == "inventory":
            character.inventory = to

    def updateWeapon(name, what, to):
        weapon = Util.loadWeapon(name)
        if what == "name":
            weapon.name = to
        if what == "attack":
            weapon.attack = to
        if what == "special":
            weapon.special = to
        if what == "crit":
            weapon.crit = to
