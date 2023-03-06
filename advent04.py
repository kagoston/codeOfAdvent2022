import sys

def fully_contain(intervals):
    """
    input: list of tuples
              containing sorted intervals in increasing order
              
    returns True if one interval includes the other one False
    otherwise
    """


    for i in range(1, len(intervals)):
        # if end of the actual interval is not greater than
        # the end of the previous interval
        second_included = intervals[i][1] <= intervals[i - 1][1]
        first_included = (intervals[i][0] == intervals[i - 1][0]
                          and intervals[i][1] > intervals[i - 1][1])
        if (first_included or second_included):
            return True
    
    return False


def overlap(intervals):
    """
    input: list of tuples
              containing sorted intervals in increasing order
              
    returns True if the two intervals overlap, False otherwise
    """

    for i in range(1, len(intervals)):
        if intervals[i][0] <= intervals[i - 1][1]:
            return True
    
    return False

def get_interval(string):
    """
    input: string containing two intervals separated by comma

    returns a list with two tuples
    containing the beginning and the end of an interval
    """
    intervals = [tuple([int(n) for n in s.split("-")]) for s in line.split(",")]

    return intervals


if __name__ == "__main__":
    """
    advent of code 2022 day 4

    check intervals for fully and partly overlapping 
    """

    # filename = "advent04.txt"
    filename = sys.argv[1]

    with open(filename, "r") as f:
        content = f.readlines()

    interval_pair = []
    counter = 0
    counter2 = 0
    for line in content:
        line = line.strip()

        interval_pair = get_interval(line)
        interval_pair.sort()
        # count the fully overlapping intervals
        counter += 1 if fully_contain(interval_pair) else 0

        # count the overlapping pairs
        counter2 += 1 if overlap(interval_pair) else 0
        
        interval_pair.clear()

    print(counter, counter2)

