#!/bin/python3
# -*- coding: utf-8 -*-

from os import listdir
from util import *
import globals
from typing import List
from dungeon import Dungeon


class Controler():
    def __init__(self):
        self.team = []
        self.length = 1
        self.dungeon = None
        self.finished = False

    def setTeam(self, team: list) -> None:
        self.team = team

    def setLength(self, length: int) -> None:
        self.length = length

    def getAllCharactersNamesList() -> List[str]:
        return [char.replace(".dat", "") for char in listdir(globals.controlable)]

    def indexToCharacter(self, index: int):
        try:
            return self.dungeon.team[index]
        except IndexError:
            return False

    def namesToCharacters(team: List[str]) -> list:
        character_team = []
        for name in team:
            character = loadCharacter(name, True)
            character_team.append(character)
        return character_team

    def initDungeon(self, enemies_pool) -> None:
        if not self.team or self.length == 1:
            print("Before starting a dungeon, you must have a team")
        else:
            self.dungeon = Dungeon(self.team, self.length, enemies_pool)

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

    def getTeamStatusStr(self) -> list:
        return [f"{character.getName()} hp: {character.getHp()}"
                for character in self.team]

    def getTeamLength(self) -> int:
        return len(self.dungeon.team)

    def initFight(self) -> bool:
        return self.dungeon.initFight()

    def setRoom(self, room) -> bool:
        if room == 'ex':
            return True
        else:
            self.dungeon.current_room = room
            return False

    def useItem(self, index) -> bool:
        return True if self.dungeon.useItemIndex(index) else False

    def getCharacterInventoryStr(self, index) -> List[str]:
        return self.dungeon.getCharacterItems(index)


def main():
    pass


if __name__ == '__main__':
    main()
