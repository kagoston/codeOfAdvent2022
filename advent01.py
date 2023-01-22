# task 1:
# Find the Elf carrying the most Calories. How many total Calories is that Elf carryin?

def read_content(filename):
    # open the file
    with open(filename, "r") as f:
        content = f.readlines()
    return content

def get_largest_sum(filename):
    '''
    for one elf: read till an empty line comes
    first convert to int then cummulate
    allways keep the higher number
    '''
    content = read_content(filename)
    currentElf = 0
    largest = 0
    for line in content:
        if line == "\n":
            #  if there is a content of a new elf, compare and keep the higher one   
            largest = largest if largest > currentElf else currentElf
            currentElf = 0
            continue
        else:
           currentElf += int(line.rstrip())

    return largest


# task 2
def get_top_three(filename):
    '''
    get the number of calories for each elf
    then sort and return the top three
    '''
    content = read_content(filename)
    currentElf = 0
    calories = []
    for line in content:
        if line == "\n":
            calories.append(currentElf)
            currentElf = 0
        else:
            currentElf += int(line.rstrip())
    
    calories.sort()

    return sum(calories[-3:])


if __name__ == "__main__":
    
    print(get_largest_sum("advent01.txt"))

    print(get_top_three("advent01.txt"))

    
