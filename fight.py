#!/bin/python3

from character import Character
from weapon import Weapon

from random import randrange
# import sys


def roll(times):
    output = 0
    for i in range(0, times):
        output += randrange(1, 7)
    return output


def testAttack(who, times=10, armor=0):
    for i in range(0, times):
        who.attack(
                who.inventory["weapon"],
                Character("dummy", 0, {"armor": armor}),
                roll(2),
                roll(2),
            )


def parseInt():
    while True:
        str = input()
        try:
            return int(str)
        except ValueError:
            print("Pass a number")


def chooseCharacter(team):
    names = []
    for member in team:
        names.append(member.getName())
        print("Choose character:")
        for i, name in enumerate(names):
            print(f"{i}. {name}")
        while True:
            try:
                return team[parseInt()]
            except IndexError:
                print("No character assigned to that number")


def chooseAction(character, team, oponent_team):
    print("Choose action:")
    print("1. Change character.")
    print("2. Attack.")
    print("3. Special attack.")
    # idea for listing items - use for items and f""
    while True:
        choice = parseInt()
        if choice == 1:
            return True
        elif choice == 2:
            print("Choose an enemy to attack:")
            for i, op in enumerate(oponent_team):
                print(f"{i}. {op}")
                # TODO finish that
            return False
        elif choice == 3:
            # special
            print("Special attack not configured")
        print("Wrong number")


def clearField(team, oponent_team):
    for i, member in enumerate(team):
        if member.isDead():
            team.pop(i)
    for i, member in enumerate(oponent_team):
        if member.isDead():
            oponent_team.pop(i)


def oponentsAction(oponent_team):
    pass


def fightControlable(team, oponent_team):
    while True:
        players_turn = True
        while players_turn:
            character = chooseCharacter(team)
            players_turn = chooseAction(character)
        clearField(team, oponent_team)
        if oponent_team.size() == 0 or team.size() == 0:
            break
        oponentsAction(oponent_team)
        clearField(team, oponent_team)
        if oponent_team.size() == 0 or team.size() == 0:
            break


def main():
    weapons = [Weapon("knife", 4, [8, 8], 9), Weapon("mace", 3, [10, 8], 10)]
    invKnife = {}
    invKnife["armor"] = 1
    knife = {}
    knife["attack"] = 4
    invKnife["weapon"] = weapons[0]

    shiv = Character("shiv", 7, invKnife)

    invMace = {}
    invMace["armor"] = 2
    mace = {}
    mace["attack"] = 3
    invMace["weapon"] = weapons[1]

    muck = Character("muck", 9, invMace)

    dummy = Character("dummy", 5, inventory={})

    team = [muck, shiv]
    op_team = [dummy, dummy]
    fightControlable[team, op_team]


if __name__ == '__main__':
    main()
