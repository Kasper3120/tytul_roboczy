#!/bin/python3

from util import Util
from weapon import Weapon
from consumable import Consumable

from os import listdir
import pdb


class Update:
    # modify accordingly to your needs
    # last mod: update (add) max_hp to hp
    def updateAllCharacters():
        list = listdir("./bin/characters/")
        for character_file in list:
            character_old = Util.loadCharacter(character_file.replace(".dat", ""))
            character_old.agility = input(f"Agility for {character_file}\n")
            Util.saveCharacter(character_old)
            print(f"updated {character_file}")

    def updateAllWeapons():
        list = listdir("./bin/items/weapons/")
        for weapon_file in list:
            weapon_old = Util.loadWeapon(weapon_file.replace(".dat", ""))
            desc = input(f"Description for {weapon_old.name}\n")
            weapon_new = Weapon(
                    weapon_old.name,
                    desc,
                    {},
                    weapon_old.attack,
                    weapon_old.special,
                    weapon_old.crit
                    )
            Util.saveWeapon(weapon_new)

    def updateCharacter(name, what, to):
        character = Util.loadCharacter(name)
        if what == "name":
            character.name = to
        if what == "hp":
            character.hp = to
        if what == "max_hp":
            character.max_hp = to
        if what == "strength":
            character.strength = to
        if what == "agility":
            character.agility = to
        if what == "status":
            character.status = to
        if what == "inventory":
            character.inventory = to
        Util.saveCharacter(character)

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
        Util.saveWeapon(weapon)


def main():
    potion = Util.loadConsumable("health potion")
    character = Util.loadCharacter("Muck")
    character.inventory.backpack = [potion]
    Util.saveCharacter(character)


if __name__ == '__main__':
    main()
