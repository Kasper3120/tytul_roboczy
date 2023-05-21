from fight import Fight
from random import randrange
from character import Character
from item import Item

from util import roll, loadCharacter, loadConsumable, parseInt
from typing import List

import pdb


class Dungeon:
    def __init__(self, team: List[Character], length: int = 5, enemies_pool: List[Character] = [], items_pool: List[Item] = []):
        self.map = {}
        # visited = []
        self.squares = ["a1", "a2"]
        self.enemies = {}
        self.chests = {}
        self.team = team
        self.length = length
        self.generateDungeon(0)
        self.enemies_pool = enemies_pool # TODO: add enemies/items_pool usage
        self.items_pool = items_pool
        self.current_room = "a1"

    def randomizeEnemies(self, num: int) -> List[Character]:
        enemies_team = []
        for i in range(0, num):
            roll_enemies = roll()
            if roll_enemies < 3:
                enemies_team.append(loadCharacter("Rat", False))
            elif roll_enemies < 5:
                enemies_team.append(loadCharacter("Spider", False))
            else:
                enemies_team.append(loadCharacter("Skeleton", False))
        return enemies_team

    def generateMap(self) -> None:
        self.map["a1"] = ["a2"]
        for i in range(2, self.length+1):
            self.map[f"a{i}"] = [f"a{i+1}", f"a{i-1}"]
            self.squares.append(f"a{i+1}")
        # generate exit
        self.map[f"a{self.length}"] = ["ex"]
        # generate small branches
        for i in range(1, int(self.length/2)):
            rand = randrange(1, self.length)
            if f"b{rand}" not in self.map[f"a{rand}"]:
                self.map[f"a{rand}"].append(f"b{rand}")
                self.map[f"b{rand}"] = [f"a{rand}"]
                self.squares.append(f"b{rand}")
            elif f"z{rand}" not in self.map[f"a{rand}"]:
                self.map[f"a{rand}"].append(f"z{rand}")
                self.map[f"z{rand}"] = [f"a{rand}"]
                self.squares.append(f"z{rand}")
            elif f"c{rand}" not in self.map[f"b{rand}"]:
                self.map[f"b{rand}"].append(f"c{rand}")
                self.map[f"c{rand}"] = [f"b{rand}"]
                self.squares.append(f"c{rand}")

    def generateDungeon(self, add: int = 0) -> None:
        self.generateMap()
        # generate enemies
        for room in self.squares:
            if roll() > 4:
                # how many enemies
                roll_enemies = roll(2)
                num = int(roll_enemies/2)
                # which enemies
                self.enemies[room] = self.randomizeEnemies(num+add)
        # if no enemies generate harder fight at the end
        if not self.enemies:
            self.enemies[f"a{self.length-1}"] = self.randomizeEnemies(8)
        # TODO: generate chests
        # hp potion in 1st room
        self.chests['a1'] = [loadConsumable("health potion")]

    def visualizeDungeon() -> int:
        # TODO: finish visualisation:
        room = "a1"
        while room != "ex":
            print(room)
            print('=')
            for turn in map["room"]:
                if turn[0] == 'a' and int(turn[1]) > int(room[1]):
                    room = turn
                else:
                    continue

    def useItemIndex(self, index) -> bool:
        try:
            # TODO chooseItem -> to model
            return self.team[index].chooseItem()
        except IndexError:
            return False

    def useItem(self) -> bool:
        print("Choose character:")
        for i, character in enumerate(self.team):
            print(f"{i}. {character.getName()}")
        print(f"{len(self.team)}. Exit")
        chosen_character = False
        while not chosen_character:
            try:
                input = parseInt()
                if input == len(self.team):
                    return False
                chosen_character = self.team[input]
            except IndexError:
                print("No character under that index")
        return chosen_character.chooseItem()

    def getChest(self, room: str) -> List[Item] or bool:
        try:
            return self.chests[room]
        except IndexError:
            print("Error! No chest in that room")
            return False

    def takeItemFromChest(self, room: str, item: Item, character: Character) -> None:
        character.pickUpItem(item)
        self.chests.pop(room)

    def openChest(self, room: str) -> bool:
        try:
            chest = self.chests[room]
        except IndexError:
            print("Error! No chest in that room")
            return False
        print("The chest contained:")
        print(chest)
        for item in chest:
            print(f"Choose character to pick up the {item.name}:")
            for i, character in enumerate(self.team):
                print(f"{i}. {character.getName()}")
            chosen_character = False
            while not chosen_character:
                try:
                    input = parseInt()
                    chosen_character = self.team[input]
                except IndexError:
                    print("No character under that index")
            chosen_character.pickUpItem(item)
        self.chests.pop(room)

    def initFight(self) -> bool:
        # pdb.set_trace()
        try:
            self.team = Fight(self.team, self.enemies[self.current_room]).aftermath()
            self.enemies.pop(self.current_room)
            return True if self.team else False
        except KeyError:
            print("Key Error: ")
            print(f"enemies.keys(): {self.enemies.keys()}")
            print(f"current_room: {self.current_room}")
            print("foo")
            exit(-1)

    # bug you can enter fight once again and enemies are already dead (>=0 hp)
    def startDungeon(self) -> None:
        self.current_room = "a1"
        while True:
            # pdb.set_trace()
            if self.current_room in self.enemies.keys():
                # TODO: inspect that bug further
                self.team = Fight(self.team, self.enemies[self.current_room]).aftermath()
                self.enemies.pop(self.current_room)
            if not self.team:
                print("You lost!")
                return
            while True:
                # choosing room
                print("team:")
                for character in self.team:
                    print(f"{character.getName()}[Hp:{character.getHp()}]")
                print("Choose a room:")
                print(self.map[self.current_room])
                print("1. Use an item")
                i = 2
                # idea: if there's a problem with indexing - add a list[index]=action
                if self.current_room in self.chests.keys():
                    print(f"{i}. Open chest")
                    i += 1
                choice = input()
                if choice in self.map[self.current_room]:
                    self.current_room = choice
                    break
                elif choice == "1":
                    self.useItem()
                elif choice == "2" and self.current_room in self.chests.keys():
                    self.openChest(self.current_room)
                else:
                    print("There's no such room near your position")
                    print("Option not found")
            if self.current_room == "ex":
                break
        print("You have managed to leave the dungeon")

    def bugEmptyfight(self) -> None:
        """
        bug solved
        generates 3 rooms one with a rat one with empty enemy team and start one
        """
        self.map["a1"] = ["a2"]
        self.map["a2"] = ["b2", "ex"]
        self.enemies = {"a2": [loadCharacter("Rat")], "b2": []}
        self.startDungeon()

    def getCharacterItems(self, index) -> List[str]:
        character = self.team[index]
        return character.getItemNamesList()

    def isCharacterIndex(self, index: int) -> bool:
        try:
            if self.team[index]:
                return True
        except IndexError:
            return False


def main():
    team = [loadCharacter("Henry"), loadCharacter("Muck")]
    dung = Dungeon(team, 7)
    dung.startDungeon()


if __name__ == '__main__':
    main()
