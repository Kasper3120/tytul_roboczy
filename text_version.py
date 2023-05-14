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
                self.newGame()
            elif choice == 4:
                exit(0)
            else:
                print("Option not available")

    def newGame(self):
        # new game
        team_names = self.chooseCharacters(num=2)
        print(team_names)
        length = self.chooseDifficulity()
        self.controler.setTeam(Controler.namesToCharacters(team_names))
        self.controler.setLength(length)
        self.controler.initDungeon(enemies_pool=['foo'])

    def chooseCharacters(self, num: int = 2) -> List[str]:
        team_names = []
        # characters (2) choice
        for i in range(0, num):
            print("Choose character (type in name):")
            # init a character list
            list = Controler.getCharacterList()
            # remove from the list characters that are already chosen
            for name in team_names:
                if name in list:
                    list.remove(name)
            # input cgaracter name
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
    def chooseDifficulity(self):
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
