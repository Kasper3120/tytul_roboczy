#!/bin/python3
# -*- coding: utf-8 -*-

from os import listdir
from typing import List
import pdb

import globals
from dungeon import Dungeon
from util import *


class Controler():
    def __init__(self):
        self.init_team = []
        self.length = 1
        self.dungeon = None
        self.finished = False

    def setTeam(self, team: list) -> None:
        self.init_team = team

    def setLength(self, length: int) -> None:
        self.length = length

    def getAllCharactersNamesList() -> List[str]:
        return [char.replace(".dat", "") for char in listdir(globals.controlable)]

    def indexToCharacter(self, index: int):
        try:
            return self.dungeon.team[index]
        except IndexError:
            return False

    def isCharacterOnIndex(self, index: int):
        try:
            if self.dungeon.team[index]:
                return True
        except IndexError:
            return False

    def namesToCharacters(team: List[str]) -> list:
        character_team = []
        for name in team:
            character = loadCharacter(name, True)
            character_team.append(character)
        return character_team

    def initDungeon(self) -> bool:
        if not self.init_team or self.length == 1:
            return False
        else:
            self.dungeon = Dungeon(self.init_team, self.length, [(loadCharacter("Rat", False), 3), (loadCharacter("Spider", False), 5), (loadCharacter("Skeleton", False), 6)] )
            return True

    def isChestInRoom(self) -> bool:
        room = self.dungeon.current_room
        return True if room in self.dungeon.chests else False

    def isFightInRoom(self) -> bool:
        room = self.dungeon.current_room
        return True if room in self.dungeon.enemies.keys() else False

    def getDirections(self) -> List[str]:
        room = self.dungeon.current_room
        if self.dungeon:
            return self.dungeon.map[room]
        else:
            return False

    def getChestNames(self, room=None):
        return self.dungeon.getChestStrList(room)

    def getTeamWithHpStr(self) -> list:
        return [f"{character.getName()} hp: {character.getHp()}"
                for character in self.dungeon.team]

    def getTeamLength(self) -> int:
        return len(self.dungeon.team)

    def isTeamDead(self) -> bool:
        """clear dead characters and return if team is dead"""
        self.dungeon.team = [character for character in self.dungeon.team if not character.isDead()]
        return not bool(self.dungeon.team)

    def initFight(self) -> bool:
        """inits fight and returns true if it was successful"""
        return self.dungeon.initFight()

    def getFightStatusControler(self) -> bool:
        """Returns false if fight is over"""
        return self.dungeon.getFightStatus()

    def setRoom(self, room_in) -> bool:
        for room in self.getDirections():
            if room_in == room :
                self.dungeon.current_room = room
                return True
            else:
                continue
        return False
            
    def isGameWon(self):
        return True if self.dungeon.current_room == "ex" else False
            

    def useItem(self, character_index, item_index) -> bool:
        """returns true if usage is successful"""
        return True if self.dungeon.useItemIndex(character_index, item_index) else False

    def getCharacterInventoryStr(self, index) -> List[str]:
        return self.dungeon.getCharacterItems(index)

    def takeItemChest(self, character_index, room=None):
        self.dungeon.takeFirstItemFromChestAllIndex(character_index)

    def deleteChest(self, room=None):
        if not room:
            room = self.dungeon.current_room
        self.dungeon.chests.pop(room)

    def getCurrentCharacterName(self):
        return self.dungeon.current_fight.current_char.getName()

    def getCurrentCharacterHP(self):
        return self.dungeon.current_fight.current_char.getHp()

    def getCurrentCharacterInventory(self):
        return self.dungeon.current_fight.current_char.getItemNamesList()

    def useItemCurrentCharacter(self, item_index):
        return True if self.dungeon.current_fight.useItemCurrentCharacter(item_index) else False

    def getEnemyTeamWithHpStr(self) -> list:
        return [f"{character.getName()} hp: {character.getHp()}"
                for character in self.dungeon.current_fight.enemy_team]

    def attackEnemy(self, chosen_enemy):
        """returns string, with attack_info and dead_info or false if there is no such target"""
        return self.dungeon.current_fight.attackEnemy(chosen_enemy)

    def takeTurnFight(self):
        """returns string to be printed or True if menu should be displayed"""
        init_output = self.dungeon.current_fight.initTurn()
        action_needed = False
        if isinstance(init_output, bool):
            return init_output
        if init_output[0]:
            action_needed = True
            # disp menu and take input
        output = []
        for info in init_output:
            if info is True or info is False:
                continue
            if isinstance(info, str):
                if info:
                    output.append(info)
            if isinstance(info, List):
                for name in info:
                    output.append(f"{name} died.")
        # return string to be printed
        # TODO: upgrade output printing (make it a list and join with \n)
        return action_needed, output

    # TODO: finish
    def executeStatus(self, character):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
