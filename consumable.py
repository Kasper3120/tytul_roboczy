#!/bin/python3

from item import Item
from character import Character
from util import saveConsumable, loadConsumable


class Consumable(Item):
    def __init__(self, name: str = "", description: str = "", passive: dict = {}, consumed: dict = {}):
        super().__init__(name, description, passive)
        self.consumed = consumed

    def __str__(self) -> str:
        return f"{self.name}:{self.description}:{self.passive}:{self.consumed}"

    def consume(self, character: Character) -> None:
        for key in self.consumed.keys():
            if key in ("heal", "bleeding", "poisoning", "hurt"):
                if self.consumed[key][0] == 0:
                    character.hp += self.consumed[key][1]
                else:
                    character.status.append([key, self.consumed[key]])
            if key in ("strength", "agility"):
                character.status.append([key, self.consumed[key]])
                if key == "strength":
                    character.strength += self.consumed[key][1]
                if key == "agility":
                    character.agility += self.consumed[key][1]


def main():
    # print("Consumable creator!")
    # name = input("Set name\n")
    # desc = input("Set desc\n")
    # cons = {}
    # cont = True
    # while cont:
    #     consumed_name = input("Set consumed_name\n")
    #     consumed_dur = int(input("Set consumed_duration\n"))
    #     consumed_points = int(input("Set consumed_points\n"))
    #     cons[consumed_name] = (consumed_dur, consumed_points)
    #     i = input("do you want to stop inputing effects (y/n)\n")
    #     if i == 'y':
    #         cont = False
    #     else:
    #         cont = True
    # consumable = Consumable(name=name, description=desc, passive={}, consumed=cons)
    # print(consumable)
    # i = input("Do you want to save that item? (y/n)")
    # if i == 'y':
    #     saveConsumable(consumable)

    consumable = loadConsumable("health potion")
    consumable.consumed = {"heal": [2, 3]}
    saveConsumable(consumable)
    print(f"modified: {consumable}")
    # TODO: popraw potke i ogarnij kreator (consumed_points powinno być {"":[\n,\n]} chyba)


if __name__ == '__main__':
    main()
