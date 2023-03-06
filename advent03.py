import sys


def find_common_item(strings):
    """
    input: sequence of strings

    finds the common character in the given strings

    returns the common item (one) in the given strings
    """
    char_no = 26

    # we use two hash arrays of size 26 (for a-z, where 0 is a, and z is 25).     
    # primary container to mark common characters
    primary = dict()
    for n in range(char_no):
        primary[chr(n + 97)] = True
        primary[chr(n + 65)] = True
 
    n = len(strings)

    for i in range(n):
        # secondary dictionary for common characters, all keys initialized false
        current = dict.fromkeys(primary.keys(), False)

        # check all the characters of the current string
        # if we have seen a character before we’ll mark it
        # if we haven’t then ignore the character because it is not a common one
        for j in strings[i].strip():
            if primary[j]:
                current[j] = True

        # update the  common items with the current ones
        for i in current.keys():
            primary[i] = current[i]

    for k, v in primary.items():
        if v == True:
            return k

      
def get_priority(c):
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    if c.isupper():
        # ascii code for A is 65, it should get priority 27, 65 - 27 = 38
        return ord(c) - 38
    else:
        # ascii code for a is 97, it should  get priority 1
        return ord(c) - 96


def sum_priorities_line(strings):
    """
    input: sequence of characters in eachl line
             two concatenated strings of equal length

    return sum of the priorities of the common characters
    
    """
    total_priority = 0
    
    for line in content:
        if  line == '':
            break
        string_size = len(line) // 2
        common_item = find_common_item((line[:string_size], line[string_size:]))
        total_priority += get_priority(common_item)

    return total_priority


def sum_priorities_bunch(strings):
    """
    Input: sequence of characters in each line
              Every set of three lines corresponds to a single group
              sum up the priorities of common items in each three-group

    returns the sum of the priorities of the common items in the groups
    """
    total_priority = 0

    for i in range(0, len(strings) - 2, 3):
        common_item = find_common_item((strings[i], strings[i+1], strings[i+2]))
        total_priority += get_priority(common_item)
        
    return total_priority


if __name__ == "__main__":
    """
    advent of code 2022 day 3
    """
    filename = sys.argv[1]
    
    with open(filename, "r") as f:
        content = f.readlines()
        # task 1
        print(sum_priorities_line(content))
    
        # task
        print(sum_priorities_bunch(content))
