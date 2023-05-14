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

    def setTeam(self, team: list) -> None:
        self.team = team

    def setLength(self, length: int) -> None:
        self.length = length

    def getCharacterList() -> List[str]:
        return [char.replace(".dat", "") for char in listdir(globals.controlable)]

    def namesToCharacters(team: List[str]) -> list:
        character_team = []
        for name in team:
            character = loadCharacter(name, True)
            character_team.append(character)
        return character_team

    def initDungeon(self, enemies_pool):
        if not self.team or self.length == 1:
            print("Before starting a dungeon, you must have a team")
        else:
            dungeon = Dungeon(self.team, self.length, enemies_pool)
            dungeon.startDungeon()


def main():
    pass


if __name__ == '__main__':
    main()
