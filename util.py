#!/bin/python3
# from character import Character

from random import randrange
import pickle


class Util:
    def roll(times):
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
