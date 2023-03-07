import re
import copy

def init_stacks(string, stacks):
    """
    input: 36 character long string
             containing capitalized letters in square brackets

    updates the stacks list in place
    """
    pattern = r"[A-Z]"
    matches = re.finditer(pattern, string)
    for m in matches:
        # the nth letters position is  on the 1 + 4*n index
        stack_id = (m.start() // 4) 
        stacks[stack_id].append(m.group())


def get_instruction(line):
    """
    input: a string with move instruction
    
    return list of three numbers: number of steps, quelle and target stack
    
    """
    pattern = r"[\d]+"
    matches = re.findall(pattern, line)
    matches = [int(m) for m in matches]
    return matches

def moveCrates(move_details, stacks):
    """
    input:
    move_details: three numbers in a list with number of steps,
                        quelle and target stack
    stacks: lists of numbers, each  representing a stack

    changes the input stacks based on the instructions in move_details
    by removing the last item in the start stack and adding it to the target
    """
    
    steps, start, target = tuple(move_details)

    for i in range(steps):
        # check if start stack is empty
        # stack ids start at 1,  idx at 0
        if not stacks[start - 1]:
            break

        stacks[target-1].append(stacks[start - 1].pop())


def moveWithOrder(moveDetails, stacks):
    """
    input:
    move_details: three numbers in a list with what to move,
                        quelle and target stack
    stacks: lists of numbers, each  representing a stack

    updates the input stacks based on the instructions by removing
    a number of items given from the start stack and adding them
    to the target stack
    """
    
    items_no, start, target = tuple(moveDetails)

    stacks[target - 1].extend(stacks[start - 1][-items_no:])
    
    for s in range(items_no):
        stacks[start - 1].pop()

    
if __name__ == "__main__":
    """
    advent of code 2022 day 5

    stack
    """
    filename = "advent05.txt"

    stack_count = 9
    stacks = [[] for _ in range(stack_count)]
    moves = []

    with open(filename, "r") as f:
        for line in f:
            if line and line[0] == "[":
                init_stacks(line, stacks)

            elif line and line[0] == "m":
               moves.append(get_instruction(line))

        for stack in stacks:
            stack.reverse()

    stacks_task1 = stacks
    stacks_task2 = copy.deepcopy(stacks)

    for moveData in moves:
           moveCrates(moveData, stacks_task1)
           moveWithOrder(moveData, stacks_task2)

    print("\ntask 1: ", end='')
    for stack in stacks_task1:
        print(stack[-1], end='')

    print("\ntask 2: ", end='')
    for stack in stacks_task2:
        print(stack[-1], end='')
        
