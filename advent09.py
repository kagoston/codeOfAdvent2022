import sys

class Rope():
    def __init__(self, startRow, startCol):
        # store the positions that the tail visited at tleast once
        self._visited = dict()

        self.head = Knot(startRow, startCol)
        self.tail = Knot(startRow, startCol)
        self.knots = [self.head, self.tail]
        self.setVisited(self.tail.row, self.tail.col)

    def processMotion(self, motion):
        """
        input: motion is a list containing two characters for direction
                 number of steps

        change the position of the object in the given direction
        """
        step = int(motion[1])
        direction = motion[0]

        for i in range(step):
            self.head.move(direction)

            for i in range(len(self.knots)-1):
                self.knots[i].pull(self.knots[i+1])

            self.setVisited(self.tail.row, self.tail.col)

        # test the steps
        # self.printTestGrid(25, 22)

    def setVisited(self, row, col):
        if self._visited.get(row, None) is None:
            self._visited[row] = set()
        self._visited[row].add(col)

    def countVisited(self):
        return sum(len(self._visited[r]) for r in self._visited.keys())

    def printTestGrid(self, width, length):
        coords = [(knot.row, knot.col) for knot in self.knots]
        for r in range(length):
            print(r, end='')
            for i in range(width):
                if r == self.head.row and i == self.head.col:
                    print("H", end='')
                elif r == self.tail.row and i == self.tail.col:
                    print("T", end='')
                elif (r, i) in coords[1:-1]:
                    print(coords.index((r, i)), end='')
                else:
                    print(".", end='')
            print("\n")

        print("\n")


class Knot(Rope):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def isCloseEnough(self, other):
        """
        the distance between two knots is close enough if the distance
        between them is smaller then 2
        """
        if abs(self.row - other.row) < 2 and abs(self.col - other.col) < 2:
            return True
        else:
            return False

    def move(self, direction):
        """
        input: character representing one of the possible directions
                  right, left, up, down
        move the knot in the given direction
        """
        if direction == "R":
            self.col += 1
        elif direction == "L":
            self.col -= 1
        elif direction == "U":
            self.row -= 1
        elif direction == "D":
            self.row += 1

    def pull(self, followerKnot):
        """
        input: two knots, one that goes first and
                 the second follows the first

        change the second objects position if the head is ever two
        steps directly up, down, left, or right from the tail, the tail
        must also move one step in that direction
        the tail moves one step diagonally to keep up with the head
        if not on the same row or column
        """

        followerMove = []
        if not self.isCloseEnough(followerKnot):
            if self.row < followerKnot.row:
                followerMove.append("U")
            elif self.row > followerKnot.row:
                followerMove.append("D")

            if self.col < followerKnot.col:
                followerMove.append("L")
            elif self.col > followerKnot.col:
                followerMove.append("R")

            for m in followerMove:
                followerKnot.move(m)


if __name__ == "__main__":
    """
    advent of code 2022, day 9
    """
    motions = []
    filename = sys.argv[1]
    with open(filename, "r") as f:
        for line in f:
            motions.append(line.strip().split())

    # task1: simulate rope movement with  knots on head and tail
    rope = Rope(4, 0)
    for motion in motions:
        rope.processMotion(motion)

    print(rope.countVisited())

    # task 2: simulate rope movement with ten knotes inclusive head and tail
    rope2 = Rope(15, 11)
    for i in range(8):
        rope2.knots.insert(1, Knot(15, 11))

    for motion in motions:
        rope2.processMotion(motion)

    print(rope2.countVisited())
