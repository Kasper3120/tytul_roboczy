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

    def __init__(self, team: List[Character], enemy_team: List[Character]):
        self.team = team
        self.enemy_team = enemy_team
        self.queue = []
        self.current_character = self.team[0]
        self.restartQueue()
        # if enemy_team and team:
        #     self.fightControlable()

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

    def getTeam(self) -> List[Character]:
        return self.team

    def isFinished(self) -> bool:
        return not (self.team and self.enemy_team)

    def restartQueue(self):
        self.queue = [[character, True, True] for character in self.team]
        self.queue += [[enemy, True, False] for enemy in self.enemy_team]
        self.queue = sorted(self.queue, key=lambda k: k[0].agility, reverse=True)
        self.team = [
                character
                for character, active, is_controlable in self.queue
                if is_controlable]
        self.enemy_team = [
                character
                for character, active, is_controlable in self.queue
                if not is_controlable
                ]
        self.current_character = self.queue[0]

    # old code
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

    def clearField(self) -> List[str]:
        # pdb.set_trace()
        before = self.team + self.enemy_team
        self.team = [member for member in self.team if not member.isDead()]
        self.enemy_team = [member for member in self.enemy_team if not member.isDead()]
        after = self.team + self.enemy_team
        comparement = [x for x in before + after if x not in before or x not in after]
        return [character.name for character in comparement]

    def enemyAction(self, enemy) -> str:  # TODO: upgrade
        # chosen_target = self.team[randrange(0, len(self.team))]
        chosen_target = random.choice(self.team)
        return enemy.attack(chosen_target, roll(2), roll(2))

    def fightControlable(self):
        # future problem - when agility is changed it can change the order
        all_chars = self.team + self.enemy_team
        all_chars = sorted(all_chars, key=lambda k: k.agility, reverse=True)
        while True:
            for character in all_chars:
                if character.status:
                    character.executeStatus()
                    self.clearField()
                    if self.isFinished():
                        return False
                if not character.isDead():
                    if character in self.team:
                        self.chooseAction(character)
                    else:
                        self.enemyAction(character)
                if self.clearField():
                    return

    def executeStatus(self, character):
        if character.status:
            character.executeStatus()
            return self.clearField()

    # TODO: main problem: communication if character dies, two copies, character in queue
    # and character in team, research that
    # change character
    # set status
    # return status changes
    # check if controlable
    # y- show what can character do
    # attack
    # n- autoattack
    # show changes
    def makeAction(self) -> bool:
        self.clearField()
        for i, character_status in enumerate(self.queue):
            character, has_attacked, is_controlable = character_status
            print(character.getName(), has_attacked, is_controlable)
            # player's action
            if not has_attacked and is_controlable:
                self.queue[i][1] = False
                return True
            # enemy's action
            elif not has_attacked:
                if character.status:
                    character.executeStatus()
                    if self.clearField():
                        return False
                self.enemyAction(character)
                self.queue[i][1] = False
                return False
            else:
                continue
        self.restartQueue()
        return False


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
