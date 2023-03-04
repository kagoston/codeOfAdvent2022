import sys

def read_content(filename):
    """
    input: txt a file containing numbers 
              an empty line represents end of a group of numbers

    returns a list containing each line in the file as a list item
    """
    with open(filename, "r") as f:
        content = f.readlines()
    return content

def get_sums(content):
    '''
    input: in string format
              an empty line represents end of a group of numbers

    the sum up the numbers between the empty lines

    returns a sorted list
    '''
    current_sum = 0
    sums = []
    for line in content:
        if line == "\n":
            sums.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line.rstrip())
    
    sums.sort()

    return sums


if __name__ == "__main__":
    """
    code of advent 2022 day 1
    """
    filename = sys.argv[1]
    content = read_content(filename)
    sums_list = get_sums(content)
    # task 1: the largest of the sums
    print(sums_list[-1])
    # task 2: sum of the three largest sums
    print(sum(sums_list[-3:]))

    
