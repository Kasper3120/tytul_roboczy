# from character import Character

from random import randrange
from os import listdir
import pickle
import globals


def roll(times: int = 1) -> int:
    output = 0
    for i in range(0, times):
        output += randrange(1, 7)
    return output


def parseInt() -> int:
    while True:
        str = input()
        try:
            return int(str)
        except ValueError:
            print("Pass a number")


def testAttack(self, who, times: int = 10, armor: int = 0) -> None:
    pass
    # TODO: change func accordingly to current fight interface
    # for i in range(0, times):
    #     who.attack(
    #             who.inventory.weapon,
    #             Character("dummy", 0, {"armor": armor}),
    #             self.roll(2),
    #             self.roll(2),
    #         )


def saveCharacter(character, controlable: bool) -> None:
    path = globals.controlable if controlable else globals.enemies
    with open(path+f'{character.getName()}.dat', 'wb') as f:
        pickle.dump(character, f)


def loadCharacter(name: str, controlable):
    path = globals.controlable if controlable else globals.enemies
    with open(path+f'{name}.dat', 'rb') as f:
        return pickle.load(f)


def saveWeapon(weapon):
    with open(globals.weapons+f'{weapon.getName()}.dat', 'wb') as f:
        pickle.dump(weapon, f)


def loadWeapon(name: str):
    with open(globals.weapons+f'{name}.dat', 'rb') as f:
        return pickle.load(f)


def saveConsumable(consumable):
    with open(globals.consumable+f'{consumable.getName()}.dat', 'wb') as f:
        pickle.dump(consumable, f)


def loadConsumable(name: str):
    with open(globals.consumable+f'{name}.dat', 'rb') as f:
        return pickle.load(f)


def weaponSearch():
    list = listdir(globals.weapons)
    while True:
        weapon = input()
        if weapon == "0":
            return
        if weapon+".dat" in list:
            return loadWeapon(weapon)
        else:
            print("No such weapon in database, try another name; type 0 to exit")


def main():
    pass


if __name__ == '__main__':
    main()
