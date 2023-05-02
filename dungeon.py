from fight import Fight
from random import randrange
from character import Character

from util import Util


class Dungeon:
    def __init__(self, team, length=5):
        self.map = {}
        # visited = []
        self.squares = ["a1", "a2"]
        self.enemies = {}
        self.team = team
        self.generateDungeon(length)

    def randomizeEnemies(self, num):
        enemies_team = []
        for i in range(0, num):
            roll = Util.roll()
            if roll < 3:
                enemies_team.append(Util.loadCharacter("Rat"))
            elif roll < 5:
                enemies_team.append(Util.loadCharacter("Spider"))
            else:
                enemies_team.append(Util.loadCharacter("Skeleton"))
        return enemies_team

    def generateMap(self, length):
        self.map["a1"] = ["a2"]
        for i in range(2, length+1):   # TODO: add turnung back
            self.map[f"a{i}"] = [f"a{i+1}"]
            self.squares.append(f"a{i+1}")
        # generate exit
        self.map[f"a{length}"] = ["ex"]
        # generate small branches
        for i in range(1, int(length/2)):
            rand = randrange(1, length)
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

    def generateDungeon(self, length):
        self.generateMap(length)
        # generate enemies
        for room in self.squares:
            if Util.roll() > 4:
                # how many enemies
                roll = Util.roll(2)
                num = int(roll/2)
                # which enemies
                self.enemies[room] = self.randomizeEnemies(num)
        # if no enemies generate harder fight at the end
        if not self.enemies:
            # enemies_team = []
            self.randomizeEnemies(8, self.enemies[f"a{length-1}"])
            # self.enemies[f"a{length}"] = enemies_team

    def visualizeDungeon():
        # to_print = []
        # while True:
        # TODO: finish visualisation:
        #   spilling method
        #   always turn left method
        pass

    def startDungeon(self):
        current_room = "a1"
        while True:
            if current_room in self.enemies.keys():
                Fight(self.team, self.enemies[current_room])
            if not self.team:
                print("You lost")
                return
            # choosing room
            print("Choose a room:")
            print(self.map[current_room])
            while True:
                choice = input()
                if choice in self.map[current_room]:
                    current_room = choice
                    break
                else:
                    print("There's no such room near your position")
            if current_room == "ex":
                break
        print("You have managed to leave the dungeon")

    # bug solved
    # generates 3 rooms one with a rat one with empty enemy team and start one
    def bugEmptyfight(self):
        self.map["a1"] = ["a2"]
        self.map["a2"] = ["b2", "ex"]
        self.enemies = {"a2": [Util.loadCharacter("Rat")], "b2": []}
        self.startDungeon()


def main():
    team = [Util.loadCharacter("Henry"), Util.loadCharacter("Muck")]
    dung = Dungeon(team, 7)
    dung.startDungeon()


if __name__ == '__main__':
    main()
