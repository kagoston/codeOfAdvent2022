import sys


def checkVisibility(treesAround, currentTree):
    """
    input:
    treesAround: list of lists with integers (the heights of the trees)
    currentTree: integer (height of the current tree)
    
    check the visibility from outside the grid:
    A tree is visible if all of the other trees between it and
    an edge of the grid are shorter than it

    returns True if at least from one direction the tree is visible
    """

    for direction in treesAround:
        maxValue = -1    # there is a tree with heigth 0
        if direction:
            maxValue = max(direction)
        if currentTree > maxValue:
            return True
    return False    

def getViewingDistance(trees, currentTree):
    """
    input: trees is a  list of integers
             currentTree is an integer
             
    returns an integer, the number of trees  that are the same height
    or taller as the current one
    """
    d = 0
    for h in trees:
        d += 1
        if h >= currentTree:
            break
    return d


def getScenicScore(treesAround, currentHeicht):
    """
    input:
    treesAround: four lists of integers (the trees in the four directions)
    currentHeight: integer (the height of the current tree)
    
    calculate scenic score, which is for each tree the viewing distance
    in all of the four directions multiplied together.

    return: integer
    """
    score = 1
    for direction in treesAround:
        score *= getViewingDistance(direction, currentHeight)
    return score
    
    
if __name__ == "__main__":
    """
    advent of code 2022, day 8
    """

    grid = []
    filename = sys.argv[1]
    with open(filename, "r") as f:
        for line in f:
            grid.append([int(i) for i in line.strip()])

    rowNum = len(grid)
    columnNum = len(grid[0])
    visibleTreeCounter = 0
    highestScenicScore = 0
    
    for i in range(rowNum):
        for j in range(columnNum):
            currentHeight = grid[i][j]
            treesRight = grid[i][j + 1:] if j < columnNum else []
            treesLeft = grid[i][j-1::-1] if j > 0 else [] 
            treesAbove = [row[j] for row in grid[i - 1::-1]] if i > 0 else []
            treesBelow = [row[j] for row in grid[i+1:]] if i < rowNum else []
            treesAround = (treesRight, treesLeft, treesAbove, treesBelow)

            visibleTreeCounter += 1 if checkVisibility(treesAround, currentHeight) else 0
            
            
            highestScenicScore = max(highestScenicScore,
                                                  getScenicScore(treesAround, currentHeight))
            
    print("counter", visibleTreeCounter)
    print("highest score", highestScenicScore)
