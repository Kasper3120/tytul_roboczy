#!/bin/python3

from character import Character
from weapon import Weapon

from random import randrange
import pickle


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


def chooseCharacter(team): # TODO: add better display (Hp: num)
    print("Choose character:")
    for i, member in enumerate(team):
        print(f"{i}. {member.getName()} ({member.getHp()})")
    while True:
        try:
            return team[parseInt()]
        except IndexError:
            print("No character assigned to that number")


def chooseAction(character, team, enemy_team):
    print("Choose action:")
    print("1. Change character.")
    print("2. Attack.")
    print("3. Special attack.")
    # idea for listing items - use for items and f""
    while True:
        choice = parseInt()
        if choice == 1:
            return True
        elif choice == 2: # TODO: choose char opt & add func interfaceAttack
            print("Choose an enemy to attack:")
            while True:
                for i, enemy in enumerate(enemy_team):
                    print(f"{i}. {enemy.getName()} ({enemy.getHp()})")
                try:
                    chosen_enemy = enemy_team[parseInt()]
                    character.attack(character.inventory["weapon"], chosen_enemy, roll(2), roll(2))
                    return False
                except IndexError:
                    print("Wrong input") # TODO: input to tab parser
                # TODO: Add interactive rolling (or not?)
        elif choice == 3:
            # special
            print("Special attack not configured")
        print("Wrong number")


def clearField(team, enemy_team):
    for i, member in enumerate(team):
        if member.isDead():
            team.pop(i)
    for i, member in enumerate(enemy_team):
        if member.isDead():
            enemy_team.pop(i)


def enemysAction(team, enemy_team): # TODO: upgrade
    enemy = enemy_team[randrange(0, len(enemy_team))]
    chosen_target = team[randrange(0, len(team))]
    enemy.attack(enemy.inventory["weapon"], chosen_target, roll(2), roll(2))


def fightControlable(team, enemy_team):
    while True:
        players_turn = True
        while players_turn:
            character = chooseCharacter(team)
            players_turn = chooseAction(character, team, enemy_team)
        clearField(team, enemy_team)
        if not enemy_team or not team:
            break
        enemysAction(team, enemy_team)
        clearField(team, enemy_team)
        if not enemy_team or not team:
            break

def saveCharacter(character):
    with open(f'./bin/characters/{character.getName()}.dat', 'wb') as f:
        pickle.dump(character, f)

def loadCharacter(name):
    with open(f'./bin/characters/{name}.dat', 'rb') as f:
        return pickle.load(f)


def main():

    shiv = loadCharacter("Shiv")
    muck = loadCharacter("Muck")

    team = [muck, shiv]

    dummy1 = loadCharacter("Dummy")
    dummy1.setName("Dummy 1")

    dummy2 = loadCharacter("Dummy")
    dummy2.setName("Dummy 2")

    rat = loadCharacter("Rat")

    op_team = [dummy1, dummy2, rat]

    #fight
    # fightControlable(team, op_team)
    print("You won")


if __name__ == '__main__':
    main()
