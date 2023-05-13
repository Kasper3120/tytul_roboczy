#!/bin/python3

from character import Character
from weapon import Weapon
from inventory import Inventory
from util import Util

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

    # TODO: add tests for that
    def executeStatus(self, character: Character) -> None:
        for status_name, status_numbers in character.status:
            status_numbers[0] -= 1
            if status_name in ("heal", "bleeding", "poisoning", "hurt"):
                for i in range(0, status_numbers[1]):
                    if character.hp != character.max_hp:
                        character.hp += 1
                if status_numbers[0] == 0:
                    # del character.status[[status_name, status_numbers]]
                    character.status.remove([status_name, status_numbers])
            if status_name == "strength":
                # TODO: think about that :)
                pass
            if status_name == "agility":
                pass

    def attackInterface(self, character: Character) -> None:
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
            choice = Util.parseInt()
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
        enemy.attack(chosen_target, Util.roll(2), Util.roll(2))

    # TODO: bug - fight finishes after 1 full turn
    # TODO: add if execStat: clearField
    def fightControlable(self):
        # pdb.set_trace()
        # future problem - when agility is changed it can change the order
        all_chars = self.team + self.enemy_team
        all_chars = sorted(all_chars, key=lambda k: k.agility, reverse=True)
        # while self.enemy_team and self.team:
        while True:
            for character in all_chars:
                if character in self.team:
                    self.executeStatus(character)
                    if self.clearField():
                        return
                    if not character.isDead():
                        self.chooseAction(character)
                else:
                    self.executeStatus(character)
                    if self.clearField():
                        return
                    if not character.isDead():
                        self.enemyAction(character)
                self.clearField()


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

    Fight.inspectTarget(shiv)
    Fight.inspectTarget(muck)
    Fight.inspectTarget(dummy1)
    Fight.inspectTarget(rat)

    # fight
    fight = Fight(team, op_team)

    print("You won")


if __name__ == '__main__':
    main()
