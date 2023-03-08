import math
import sys

# What is the sum of the total sizes of  directories?

# input: a tree of files 
# / : outermost directory


class Node:
    def __init__(self, name):
        self.name = name
        self.children = None
        self.parent = None
        self.level = 0
        self.size = 0
        self.nodeType = ''
        
class Tree:
    def __init__(self):
        self.root = Node("/")
        self.root.nodeType = "dir"
        self.nodes = {"/": self.root}

    def addNode(self, content, parentDir):
        """
        input:
        content: list of strings 
        add the content of the current directory to the filesystem
        """
        if self.nodes.get(content[1], None) != None:
            return

        nodetype = "file" if content[0].isdigit() else "dir"
        size = '0' if nodetype == "dir" else content[0]
        name = content[1]

        newNode = Node(name)
        newNode.nodeType = nodetype
        newNode.parent = parentDir
        newNode.level = parentDir.level + 1

        # add as child to parent directory
        if parentDir.children == None:
            parentDir.children = []
            
        parentDir.children.append(newNode)

        # store the size
        if nodetype != "dir":
            newNode.size = int(size)

        # in all parent directories
        parent = newNode.parent
        while parent is not None:
            parent.size += newNode.size
            parent = parent.parent


    def getWorkingDir(self, content, currentDir):
        # cd / switches the current directory to the outermost directory
        if  content[2] == "/":
            currentDir = self.root

        # cd .. moves out one level
        elif content[2] == "..":
            currentDir = currentDir.parent if currentDir.parent != None else self.root

        # cd x moves in one level
        elif currentDir.children:
            for c in  currentDir.children:
                if content[2] == c.name:
                    currentDir = c
                    break
                else:
                    continue

        return currentDir


    def byname(self, node):
        """
        helping function for sorting names
        """
        return node.name


    def printTree(self):
        stack = [self.root,]
        while stack:
            n = stack.pop()

            level = n.level
            print(level * "- ", n.name, n.size, n.nodeType)
            if not n.children:
                continue
            else:
                n.children.sort(reverse=True, key=self.byname)
                for child in n.children:
                    stack.append(child)

    def fillFilesystem(self, filename):
        """
        input: a textfile with terminal output
            lines that begin with $ are commands
            ls prints out all of the files and directories
            immediately contained by the current directory
            lines without $ at the beginning listing the content of a directory

        create the filesystem by the content of the file
        """
        currentDir = self.root
        with open(filename, "r") as f:
            for line in f:
                content = line.strip().split()

                if content[0] == "$" and content[1] == "cd":
                    currentDir = filesystem.getWorkingDir(content, currentDir)

                elif content[0] == "$" and content[1] == "ls":
                    continue
                elif content[0] != "$":
                    filesystem.addNode(content, currentDir)

    # filesystem.printTree()


if __name__ == "__main__":
    """
    advent of code 2022, day 7
    """

    # filename = "advent07.txt"

    filename = sys.argv[1]
    filesystem = Tree()
    currentDir = filesystem.root

    filesystem.fillFilesystem(filename)
    
    # task 1: find all directories with a total size of at most 100000
    totalsize = 0
    
    stack = [filesystem.root, ]
    # depth first traversal
    while stack:
        n = stack.pop()
        if n.size <= 100000 and n.nodeType == "dir":
            totalsize += n.size
        if not n.children:
            continue
        else:
            for child in n.children:
                stack.append(child)

    print("totalsize", totalsize)

    # task 2: Find the smallest directory that, if deleted,
    # would free up enough space on the filesystem to run the update
    totalDiskSpace = 70000000
    freeSpace = totalDiskSpace - filesystem.root.size
    spaceForUpdate = 30000000
    minSpaceToFreeUp = spaceForUpdate - freeSpace
    stack2 = [filesystem.root,]
    smallest = math.inf
    
    while stack2:
        m = stack2.pop()
        if m.nodeType == "dir" and m.size >= minSpaceToFreeUp:
            smallest = min(smallest, m.size)
        if not m.children:
            continue
        else:
            for child in m.children:
                stack2.append(child)
    print('smallest dir', smallest)
        
    

            
           
                    

                

