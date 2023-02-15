
def get_final(filename, strategy = False):
    '''
    input: the strategy played

    output: final score of playing Rock Paper Scissors

    '''
    with open(filename, "r") as f:
        content = f.readlines()

    # The first column: the opponent's choice
    # A for Rock,
    # B for Paper,
    # C for Scissors.
    firstColumn = {"A" : 1, "B": 2, "C" : 3}

    # second column: your choice if there is no strategy
    # X for Rock,
    # Y for Paper
    # Z for Scissors.
    secondColumn = {"X" : 1, "Y": 2, "Z" : 3}
    scores = 0  
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    for line in content:
        shapes = line.split()
        opponentChoice = firstColumn[shapes[0]]
        yourChoice = get_shape(opponentChoice, shapes[1]) if strategy else secondColumn[shapes[1]]
        scores += get_score(yourChoice, opponentChoice)

    return scores


def get_score(yourShape, opponentShape):
    '''
    input: shapes chosen in a single round
    
    The score for a single round is the sum of the followings:
    score for the selected shape: 1 for Rock, 2 for Paper, and 3 for Scissors
    score for the outcome: 0 if you lost, 3 if the round was a draw, and 6 if you won

    output: a score of a single round
    '''
    diff = yourShape - opponentShape
    # lost
    score = yourShape
    # draw
    if opponentShape == yourShape:
        score += 3
    # win
    elif diff == 1 or diff == -2:
        score += 6
    return score           


def get_shape(opponentShape, aim):
    '''
    input: the opponents shape and the aimed outcome
    
    output: your shape to choose
    '''
    # secret strategy:
    # X means you need to lose,
    if aim == "X":
        result = (opponentShape  - 1) if opponentShape  > 1 else 3
    # Y means you need to end the round in a draw,
    elif aim == "Y":
        result =  opponentShape
    # Z means you need to win.
    else:
        result = 1 + opponentShape % 3
    
    return result
    

if __name__ == "__main__":
    print(get_final("advent02.txt"))

    print(get_final("advent02.txt", True))
