#!/bin/python3

from character import Character
from weapon import Weapon
from inventory import Inventory
from util import roll, parseInt, loadCharacter

from typing import List
from random import randrange
import random
import pdb


class Fight:

    def __init__(self, team: List[Character], enemy_team: List[Character]) -> None:
        self.team = team
        self.enemy_team = enemy_team
        if enemy_team and team:
            self.fightControlable()

    def attackInterface(self, character: Character) -> None:
        print("Choose an enemy to attack:")
        while True:
            for i, enemy in enumerate(self.enemy_team):
                print(f"{i}. {enemy.getName()} ({enemy.getHp()})")
            try:
                chosen_enemy = self.enemy_team[parseInt()]
                character.attack(chosen_enemy, roll(2), roll(2))
                break
            except IndexError:
                print("Wrong input")

    def inspectTarget(target: Character) -> None:
        print(target)

    def aftermath(self) -> List[Character]:
        return self.team

    def chooseAction(self, character: Character) -> None:
        while True:
            print(f"{character.getName()}'s turn. Hp:{character.hp}")
            print("Choose action:")
            print("1. Attack.")
            print("2. Special attack.")
            print("3. Choose item")
            choice = parseInt()
            if choice == 1:
                self.attackInterface(character)
                return
            elif choice == 2:
                # TODO: special
                print("Special attack not configured")
            elif choice == 3:
                if character.chooseItem():
                    return
            else:
                print("Wrong input")

    def clearField(self) -> bool:
        # pdb.set_trace()
        before = self.team + self.enemy_team
        self.team = [member for member in self.team if not member.isDead()]
        self.enemy_team = [member for member in self.enemy_team if not member.isDead()]
        after = self.team + self.enemy_team
        comparement = [x for x in before + after if x not in before or x not in after]
        for character in comparement:
            print(f"{character.name} died")
        return not (self.team and self.enemy_team)

    def enemyAction(self, enemy):  # TODO: upgrade
        # chosen_target = self.team[randrange(0, len(self.team))]
        chosen_target = random.choice(self.team)
        enemy.attack(chosen_target, roll(2), roll(2))

    def fightControlable(self):
        # future problem - when agility is changed it can change the order
        all_chars = self.team + self.enemy_team
        all_chars = sorted(all_chars, key=lambda k: k.agility, reverse=True)
        while True:
            for character in all_chars:
                if character.status:
                    character.executeStatus()
                    if self.clearField():
                        return
                if not character.isDead():
                    if character in self.team:
                        self.chooseAction(character)
                    else:
                        self.enemyAction(character)
                if self.clearField():
                    return


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

    Fight.inspectTarget(shiv)
    Fight.inspectTarget(muck)
    Fight.inspectTarget(dummy1)
    Fight.inspectTarget(rat)

    # fight
    fight = Fight(team, op_team)

    print("You won")


if __name__ == '__main__':
    main()
