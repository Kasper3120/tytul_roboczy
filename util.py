# from character import Character

from random import randrange
from os import listdir
import pickle


class Util:
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
    # TODO: choose character!!!

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

    def saveCharacter(character) -> None:
        with open(f'./bin/characters/{character.getName()}.dat', 'wb') as f:
            pickle.dump(character, f)

    def loadCharacter(name: str):
        with open(f'./bin/characters/{name}.dat', 'rb') as f:
            return pickle.load(f)

    def saveWeapon(weapon):
        with open(f'./bin/items/weapons/{weapon.getName()}.dat', 'wb') as f:
            pickle.dump(weapon, f)

    def loadWeapon(name: str):
        with open(f'./bin/items/weapons/{name}.dat', 'rb') as f:
            return pickle.load(f)

    def saveConsumable(consumable):
        with open(f'./bin/items/consumable/{consumable.getName()}.dat', 'wb') as f:
            pickle.dump(consumable, f)

    def loadConsumable(name: str):
        with open(f'./bin/items/consumable/{name}.dat', 'rb') as f:
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


def main():
    pass


if __name__ == '__main__':
    main()
