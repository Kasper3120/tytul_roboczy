#!/bin/python3
# -*- coding: utf-8 -*-

from controler import Controler
from util import parseInt
from consumable import Consumable

from typing import List
from sys import exit


class TextVersion():
    def __init__(self):
        self.controler = Controler()
        # print main menu
        while True:
            print(
                "1. New Game",
                "2. Load Game",
                "3. Settings",
                "4. Exit",
                sep='\n'
                  )
            # input
            choice = parseInt()
            if choice == 1:
                if self.newGame():
                    print("You have successfully escaped the dungeon")
                else:
                    print("You have been defeated")
            elif choice == 4:
                exit(0)
            else:
                print("Option not available")

    def printTeamStatusEnum(self):
        status_list = self.controler.getTeamStatusStr()
        print("Team:")
        for i, status in enumerate(status_list):
            print(f"{i}. {status}")

    def chooseCharacter(self):
        print("Choose character:")
        self.printTeamStatusEnum()
        team_len = self.controler.getTeamLength()
        print(f"{team_len}. Exit")
        while True:
            character_index = parseInt()
            if self.controler.
                break
            elif character_index == team_len:
                break
            else:
                continue

    def roomMenu(self) -> bool:
        directions = self.controler.getDirections()
        self.printTeamStatusEnum()
        print("Choose a room:")
        print(', '.join(directions))
        print("1. Use an item")
        i = 2
        if self.controler.isChestInRoom():
            print(f"{i}. Open chest")
            i += 1
        while True:
            choice = input()
            if choice in directions:
                return True if self.controler.setRoom(choice) else False
            elif choice == "1":
                character = self.chooseCharacter()
            elif choice == "2" and self.current_room in self.chests.keys():
                self.openChest(self.current_room)
            else:
                print("There's no such room near your position")
                print("Option not found")

    def newGame(self) -> bool:
        # new game
        team_names = self.chooseCharacters(num=1)
        print(team_names)
        length = self.chooseDifficulity()
        self.controler.setTeam(Controler.namesToCharacters(team_names))
        self.controler.setLength(length)
        self.controler.initDungeon(enemies_pool=['foo'])
        while True:
            if self.controler.isFightInRoom:
                if not self.controler.initFight():
                    return False
            if self.roomMenu():
                return True

    def chooseCharacters(self, num: int = 2) -> List[str]:
        team_names = []
        # characters (2) choice
        for i in range(0, num):
            print("Choose character (type in name):")
            # init a character list
            list = Controler.getAllCharactersNamesList()
            # remove from the list characters that are already chosen
            for name in team_names:
                if name in list:
                    list.remove(name)
            # input character name
            while True:
                for character in list:
                    print(character)
                choice = input()
                if choice.title() in list:
                    team_names.append(choice)
                    break
                else:
                    print("No such character")
        return team_names

    # TODO: difficulity sensitive enemies_pool
    def chooseDifficulity(self) -> int:
        while True:
            choice = input("Choose difficulity: 1-easy, 2-medium, 3-hard, 4-nightmare")
            if choice in ('easy', '1'):
                return 3
            elif choice in ('medium', '2'):
                return 5
            elif choice in ('hard', '3'):
                return 7
            elif choice in ('nightmare', '4'):
                return 9
            else:
                print("wrong input")


def main():
    TextVersion()


if __name__ == '__main__':
    main()
