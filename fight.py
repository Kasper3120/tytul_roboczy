#!/bin/python3

from character import Character
from weapon import Weapon
from inventory import Inventory
from util import Util

from random import randrange
# import pdb


class Fight:

    def __init__(self, team, enemy_team):
        self.team = team
        self.enemy_team = enemy_team
        if enemy_team and team:
            self.fightControlable()

    def executeStatus(character):
        for status_name, status_numbers in character.status:
            status_numbers[0] -= 1
            if status_name in ("heal", "bleeding", "poisoning", "hurt"):
                character += status_numbers[1]
                if status_numbers[0] == 0:
                    character.status.pop(status_name)
            if status_name in ("strength", "agility"):
                if status_numbers[0] == -1:
                    character.status.pop(status_name)

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
                print("Wrong input")

    def inspectTarget(target):
        print(target)

    def chooseAction(self, character):
        print(f"{character.getName()}'s turn")
        print("Choose action:")
        print("1. Attack.")
        print("2. Special attack.")
        print("3. Choose item")
        # idea for listing items - use for items and f""
        while True:
            choice = Util.parseInt()
            if choice == 1:
                self.attackInterface(character)
                return
            elif choice == 2:
                # TODO: special
                print("Special attack not configured")
            elif choice == 3:
                print("Items not configured")
            print("Wrong input")

    def clearField(self):
        for i, member in enumerate(self.team):
            if member.isDead():
                print(f"{member.getName()} dies")
                self.team.pop(i)
        for i, member in enumerate(self.enemy_team):
            if member.isDead():
                print(f"{member.getName()} dies")
                self.enemy_team.pop(i)

    def enemysAction(self, enemy):  # TODO: upgrade
        chosen_target = self.team[randrange(0, len(self.team))]
        enemy.attack(chosen_target, Util.roll(2), Util.roll(2))

    def players_turn():
        pass

    # def fightControlable(self):
    #     while True:
    #         players_turn = True
    #         while players_turn:
    #             character = self.chooseCharacter()
    #             players_turn = self.chooseAction(character)
    #         self.clearField()
    #         if not self.enemy_team or not self.team:
    #             break
    #         self.enemysAction()
    #         self.clearField()
    #         if not self.enemy_team or not self.team:
    #             break

    def fightControlable(self):
        # while True:
        all_chars = self.team + self.enemy_team
        all_chars = sorted(all_chars, key=lambda k: k.agility, reverse=True)
        while True:
            for character in all_chars:
                if character in self.team:
                    self.chooseAction(character)
                else:
                    self.enemysAction(character)
                self.clearField()
                if not self.enemy_team or not self.team:
                    return


def main():

    shiv = Util.loadCharacter("Shiv")
    muck = Util.loadCharacter("Muck")

    team = [muck, shiv]

    dummy1 = Util.loadCharacter("Dummy")
    dummy1.setName("Dummy 1")

    dummy2 = Util.loadCharacter("Dummy")
    dummy2.setName("Dummy 2")

    rat = Util.loadCharacter("Rat")

    op_team = [dummy1, dummy2, rat]

    # Fight.inspectTarget(shiv)
    # Fight.inspectTarget(muck)
    # Fight.inspectTarget(dummy1)
    # Fight.inspectTarget(rat)

    # fight
    fight = Fight(team, op_team)


    print("You won")


if __name__ == '__main__':
    main()
