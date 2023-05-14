#!/bin/python3

from util import *
from weapon import Weapon
from consumable import Consumable
from character import Character
from inventory import Inventory

import globals

from os import listdir
import pdb


class Update:
    # modify accordingly to your needs
    # last mod: update (add) max_hp to hp
    def updateAllCharacters(controlable: bool):
        path = globals.controlable if controlable else globals.enemies
        list = [char.replace(".dat", "") for char in listdir(path)]
        for character_name in list:
            old_char = loadCharacter(character_name)
            character_new = Character(
                    old_char.name, old_char.hp,
                    Inventory(old_char.inventory.weapon, old_char.inventory.armor, []),
                    old_char.strength, old_char.agility, []
                    )
            saveCharacter(character_new)
            print(f"updated {character_name}")

    def updateAllWeapons():
        list = listdir(globals.weapons)
        for weapon_file in list:
            weapon_old = loadWeapon(weapon_file.replace(".dat", ""))
            desc = input(f"Description for {weapon_old.name}\n")
            weapon_new = Weapon(
                    weapon_old.name,
                    desc,
                    {},
                    weapon_old.attack,
                    weapon_old.special,
                    weapon_old.crit
                    )
            saveWeapon(weapon_new)

    def updateCharacter(name: str, what: str, to):
        character = loadCharacter(name)
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
        saveCharacter(character)

    def updateWeapon(name: str, what: str, to: str):
        weapon = loadWeapon(name)
        if what == "name":
            weapon.name = to
        if what == "attack":
            weapon.attack = to
        if what == "special":
            weapon.special = to
        if what == "crit":
            weapon.crit = to
        saveWeapon(weapon)


def main():
    pass

if __name__ == '__main__':
    main()
