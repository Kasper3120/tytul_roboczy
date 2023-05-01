#!/bin/python3

from character import Character
from weapon import Weapon
from inventory import Inventory
from util import Util

from random import randrange


class Fight:

    def __init__(self, team, enemy_team):
        self.team = team
        self.enemy_team = enemy_team
        if enemy_team and team:
            self.fightControlable()

    def chooseCharacter(self):
        print("Choose a character:")
        for i, member in enumerate(self.team):
            print(f"{i}. {member.getName()} (Hp: {member.getHp()})")
        while True:
            try:
                return self.team[Util.parseInt()]
            except IndexError:
                print("No character assigned to that number")

    def attackInterface(self, character):
        print("Choose an enemy to attack:")
        while True:
            for i, enemy in enumerate(self.enemy_team):
                print(f"{i}. {enemy.getName()} ({enemy.getHp()})")
            try:
                chosen_enemy = self.enemy_team[Util.parseInt()]
                character.attack(chosen_enemy, Util.roll(2), Util.roll(2))
                break
            except IndexError:
                print("Wrong input")  # TODO: input to tab parser
            # TODO: Add interactive rolling (or not?)

    def inspectTarget(target):
        print(target)

    def chooseAction(self, character):
        print("Choose action:")
        print("1. Change character.")
        print("2. Attack.")
        print("3. Special attack.")
        # idea for listing items - use for items and f""
        while True:
            choice = Util.parseInt()
            if choice == 1:
                return True
            elif choice == 2:  # TODO: choose char opt & add func interfaceAttack
                self.attackInterface(character)
                return False
            elif choice == 3:
                # TODO: special
                print("Special attack not configured")
            print("Wrong number")

    def clearField(self):
        for i, member in enumerate(self.team):
            if member.isDead():
                self.team.pop(i)
        for i, member in enumerate(self.enemy_team):
            if member.isDead():
                self.enemy_team.pop(i)

    def enemysAction(self):  # TODO: upgrade
        enemy = self.enemy_team[randrange(0, len(self.enemy_team))]
        chosen_target = self.team[randrange(0, len(self.team))]
        enemy.attack(chosen_target, Util.roll(2), Util.roll(2))

    def fightControlable(self):
        while True:
            players_turn = True
            while players_turn:
                character = self.chooseCharacter()
                players_turn = self.chooseAction(character)
            self.clearField()
            if not self.enemy_team or not self.team:
                break
            self.enemysAction()
            self.clearField()
            if not self.enemy_team or not self.team:
                break


def main():

    # shiv = Util.loadCharacter("Shiv")
    # muck = Util.loadCharacter("Muck")

    # team = [muck, shiv]

    # dummy1 = Util.loadCharacter("Dummy")
    # dummy1.setName("Dummy 1")

    # dummy2 = Util.loadCharacter("Dummy")
    # dummy2.setName("Dummy 2")

    # rat = Util.loadCharacter("Rat")

    # op_team = [dummy1, dummy2, rat]

    # Fight.inspectTarget(shiv)
    # Fight.inspectTarget(muck)
    # Fight.inspectTarget(dummy1)
    # Fight.inspectTarget(rat)

    # fight
    # fight = Fight(team, op_team)

    
    print("You won")


if __name__ == '__main__':
    main()
