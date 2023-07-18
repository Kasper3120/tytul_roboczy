#!/bin/python3
# -*- coding: utf-8 -*-

from controler import Controler
from util import parseInt
from consumable import Consumable

from typing import List
from sys import exit
import pdb


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
        status_list = self.controler.getTeamWithHpStr()
        print("Team:")
        for i, status in enumerate(status_list):
            print(f"{i}. {status}")

    def chooseCharacterIndexTest(self) -> int:
        print("Choose character:")
        self.printTeamStatusEnum()
        team_len = self.controler.getTeamLength()
        print(f"{team_len}. Exit")
        while True:
            character_index = parseInt()
            if self.controler.isCharacterOnIndex(character_index):
                return character_index
            elif character_index == team_len:
                return -1
            else:
                continue

    def useItem(self):
        character_index = self.chooseCharacterIndexTest()
        if character_index != -1:
            item_list = self.controler.getCharacterInventoryStr(character_index)
            for i, item in enumerate(item_list):
                print(f"{i}. {item}")
            print(f"{len(item_list)}. Exit")
            while True:
                item_index = parseInt()
                if item_index == len(item_list):
                    break
                elif self.controler.useItem(character_index, item_index):
                    print("Item consumed")
                    break
                else:
                    print("Wrong input")
        else:
            print("Wrong input")

    def roomMenu(self) -> bool:
        while True:
            directions = self.controler.getDirections()
            directions = ', '.join(directions)
            self.printTeamStatusEnum()
            print("Choose a room:")
            print(directions)
            print("1. Use an item")
            i = 2
            is_chest = self.controler.isChestInRoom()
            if is_chest:
                print(f"{i}. Open chest")
                i += 1
            choice = input()
            if choice == "1":
                self.useItem()
            elif choice == "2" and is_chest:
                self.openChest()
            elif self.controler.isRoomInDirections(choice):
                return True if self.controler.setRoom(choice) else False
            else:
                print("There's no such room near your position")
                print("Option not found")

    def openChest(self):
        """
        uses current_room
        displays all items in chest
        asks who should take each item
        passes that information further
        """
        item_list = self.controler.getChestNames()
        print("Items inside:")
        for item in item_list:
            print(item)
        for item in item_list:
            while True:
                print(f"Who should take {item}?")
                choice = self.chooseCharacterIndexTest()
                if choice != -1:
                    self.controler.takeItemChest(choice)
                    break
                else:
                    print("Wrong input")
            self.controler.deleteChest()

    def fightView(self):
        """
        init fight
        while true:
            for character in sorted
                whose turn?
                players:
                    choose target or use item
        """
        if not self.controler.initFight():
            return False
        while not self.controler.getFightStatusControler():
            if self.controler.takeTurnFight():
                pass # print menu for attacking
            else:
                pass # print enemies damages, etc

    def newGame(self) -> bool:
        # new game
        team_names = self.chooseCharacters(num=1)
        print(team_names)
        length = self.chooseDifficulity()
        self.controler.setTeam(Controler.namesToCharacters(team_names))
        self.controler.setLength(length)
        if not self.controler.initDungeon(enemies_pool=['foo']):
            print("Before starting a dungeon, you must have a team")
            return
        while True:
            if self.controler.isFightInRoom():
                self.fightView()
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
