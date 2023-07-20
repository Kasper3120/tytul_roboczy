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
        self.current_char = self.team[0]
        self.current_char_index = 0
        self.restartQueue()
        # if enemy_team and team:
        #     self.fightControlable()

    # old code
    """
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
    """

    def getTeam(self) -> List[Character]:
        return self.team

    def isFinished(self) -> bool:
        return not (self.team and self.enemy_team)

    # after whole queue
    def restartQueue(self):
        """remakes queue, function sets activity value True, queue remains unsorted"""
        self.queue = [[character, True, True] for character in self.team]
        self.queue += [[enemy, True, False] for enemy in self.enemy_team]

    # after every move
    def sortQueue(self) -> List[str]:
        """sorts queue, and removes dead characters from teams
        returns dead characters names"""
        # sorting queue
        self.queue = sorted(self.queue, key=lambda k: k[0].agility, reverse=True)
        # save queue_characters to teams and delete dead characters
        return self.clearField()

    def clearField(self):
        before = self.team + self.enemy_team
        self.team = [
                character
                for character, active, is_controlable in self.queue
                if is_controlable and not character.isDead()]
        self.enemy_team = [
                character
                for character, active, is_controlable in self.queue
                if not is_controlable and not character.isDead()]
        after = self.team + self.enemy_team
        comparement = [character.name for character in before + after if character not in after]
        return comparement

    # old code
    """
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
    """

    def enemyAction(self, enemy):  # TODO: upgrade
        # chosen_target = self.team[randrange(0, len(self.team))]
        chosen_target = random.choice(self.team)
        attack_info = enemy.attack(chosen_target, roll(2), roll(2))
        dead_info = self.sortQueue()
        return attack_info, dead_info

    # old code
    """
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
    """

    def executeStatus(self, character):
        if character.status:
            status_info = character.executeStatus()
            dead_info = self.sortQueue()
            return status_info, dead_info
        else:
            return "", []

    def useItemCurrentCharacter(self, item_index) -> bool:
        try:
            return True if self.current_char.consumeItemIndex(item_index) else False
        except IndexError:
            return False

    def attackEnemy(self, chosen_enemy):
        attack_info = self.current_char.attack(self.enemy_team[chosen_enemy], roll(2), roll(2))
        dead_info = self.sortQueue()
        return attack_info, dead_info

    # status applying isn't finished
    def initTurn(self) -> bool:
        """return patterns:
            True, status_info - display menu for self.current_char + status_info
            False, status_info, dead_info_status - char died because of status + status_info
            False, status_info, dead_info_status, attack_info, dead_info_attack -
            - dead_info_status died, enemy attacked and killed dead_info_attack"""
        self.sortQueue()
        # look for someone who havent attacked yet
        for i, char_in_queue in enumerate(self.queue):
            character, is_active, is_controlable = char_in_queue
            status_info = ""
            # player's action
            if is_active and is_controlable:
                status_info, dead_info_status = self.executeStatus(character)
                if status_info:
                    if character.name in dead_info_status:
                        # no input needed, who died
                        return False, status_info, dead_info_status
                else:
                    self.current_char = self.queue[i][0]
                    self.queue[i][1] = False
                    return True, status_info
            # enemy's action
            elif is_active:
                status_info, dead_info_status = self.executeStatus(character)
                if character.name in dead_info_status:
                    # no input needed, who died
                    return False, status_info, dead_info_status
                self.queue[i][1] = False
                # return False - no action needed, who died because of status,
                # who was attacked, who died because of attack
                attack_info, dead_info_attack = self.enemyAction(self.queue[i][0])
                return False, status_info, dead_info_status, attack_info, dead_info_attack
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
