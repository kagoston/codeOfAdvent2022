import sys

def get_input(filename):
    with open(filename, "r") as f:
        content = f.read()
    return content

def check_unique_characters(string):
    """
    determine if a string has all unique characters
    """
    # maintain a boolean array for the characters
    # only lowercase characters
    chars_n = 26
    chars = [False] * chars_n
    for i in range(len(string)):
        # ascii code for a is 97
        index = ord(string[i]) - 97
        if chars[index] == True:
            return False
        else:
            chars[index] = True

    return True  

    
if __name__ == "__main__":
    """
    advent of code 2022, day 6

    determine if a string has all unique characters
    
    """
    # filename = "advent06.txt"
    filename = sys.argv[1]
    content = get_input(filename)

    # task: identify the position of the last character in a string 
    # where the last n characters are all different.

    unique_chars_n = 4
    total_chars = len(content)

    # task 1
    for i in range(unique_chars_n, len(content)):
        if check_unique_characters(content[i - unique_chars_n:i]):
            print(i)
            break
    # task 2
    unique_chars_n = 14
    for i in range(unique_chars_n, len(content)):
        if check_unique_characters(content[i - unique_chars_n:i]):
            print(i)
            break
    


                
