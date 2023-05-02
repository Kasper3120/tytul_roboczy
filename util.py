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
        with open(f'./bin/items/weapons/{weapon.getName()}.dat', 'wb') as f:
            pickle.dump(weapon, f)

    def loadConsumable(name):
        with open(f'./bin/items/consumable/{name}.dat', 'rb') as f:
            return pickle.load(f)

    def saveConsumable(consumable):
        with open(f'./bin/items/consumable/{consumable.getName()}.dat', 'wb') as f:
            pickle.dump(consumable, f)

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


def main():
    pass


if __name__ == '__main__':
    main()
