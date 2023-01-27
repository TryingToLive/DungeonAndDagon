from random import randint, choice

class Map_Grid():
    """in this class we identify the attributes for map grid
    and we init the different variables in the game"""

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.walls = []
        self.start = (0, 0)
        self.goal = (18, 18)
        self.player = (0, 0)
        self.shop = (9, 9)

    def draw_grid(self, width=2):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in graph.walls:
                    symbol = "🟥"
                elif (x, y) == self.shop:
                    symbol = "🏠"
                elif (x, y) == self.player:
                    symbol = "★  "
                elif (x, y) == self.start:
                    symbol = "<  "
                elif (x, y) == self.goal:
                    symbol = "🚩"
                else:
                    symbol = "🟩"
                print("%%-%ds" % width % symbol, end="")
            print()

    def get_walls(self, pct=0.25) -> list:
        out = []
        for _ in range(int((self.height * self.width * pct) // 2)):
            x = randint(1, self.width - 2)
            y = randint(1, self.height - 2)
            out.append((x, y))
            out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
            if (9, 9) in out:
                out.remove((9, 9))
            if (18, 18) in out:
                out.remove((18, 18))
            if (1, 1) in out:
                out.remove((1, 1))
            if (9, 8) in out:
                out.remove((9, 8))
            if (17, 18) in out:
                out.remove((17, 18))
        return out
        
graph = Map_Grid(19, 19)
