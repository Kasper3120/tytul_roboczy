#!/bin/python3
# -*- coding: utf-8 -*-

from os import listdir
from util import *
import globals
from typing import List
from dungeon import Dungeon


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

    def isRoomInDirections(self, user_input):
        # is user_input in directions doesn't work properly due to List[str]
        for room in self.getDirections():
            if user_input:
                return True
            else:
                continue
        return False

    def namesToCharacters(team: List[str]) -> list:
        character_team = []
        for name in team:
            character = loadCharacter(name, True)
            character_team.append(character)
        return character_team

    def initDungeon(self, enemies_pool) -> bool:
        if not self.init_team or self.length == 1:
            return False
        else:
            self.dungeon = Dungeon(self.init_team, self.length, enemies_pool)
            return True

    def isChestInRoom(self) -> bool:
        room = self.dungeon.current_room
        return True if room in self.dungeon.chests else False

    def isFightInRoom(self) -> bool:
        room = self.dungeon.current_room
        return True if room in self.dungeon.enemies else False

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

    def initFight(self) -> bool:
        return self.dungeon.initFight()

    def getFightStatusControler(self):
        return self.dungeon.getFightStatus()

    def setRoom(self, room) -> bool:
        if room == 'ex':
            return True
        else:
            self.dungeon.current_room = room
            return False

    def useItem(self, character_index, item_index) -> bool:
        return True if self.dungeon.useItemIndex(character_index, item_index) else False

    def getCharacterInventoryStr(self, index) -> List[str]:
        return self.dungeon.getCharacterItems(index)

    def takeItemChest(self, character_index, room=None):
        self.dungeon.takeFirstItemFromChestAllIndex(character_index)

    def deleteChest(self, room=None):
        if not room:
            room = self.dungeon.current_room
        self.dungeon.chests.pop(room)

    def takeTurnFight(self):
        if self.dungeon.current_fight.makeAction():
            return True
        else:
            return False
    # TODO: finish
    def executeStatus(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
