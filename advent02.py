import sys

def play_tournament(rounds, strategy=False):
    """
    input:
    
    rounds: two letters in each line as one round in the game
                letters represents the shape chosen by the opponent
                and the player 
    strategy: whether to use the player input as an intended outcome

    returns the total score for the whole game
    """
    
    total_score = 0
    for move in rounds:
        shapes = move.split()
        total_score += get_score2(shapes[0], shapes[1], strategy)

    print(total_score)

def get_score2(opponent_choice, player_choice, strategy):
    """
    Input:
    opponent: A for Rock, B for Paper, and C for Scissors
    player: X for Rock, Y for Paper, and Z for Scissors
    
    The score for a single round is the sum of the followings:
    score for the selected shape: 1 for Rock, 2 for Paper, and 3 for Scissors
    score for the outcome: 0 if you lost, 3 if the round was a draw, and 6 if you won
    
    output: a score of a single round
    """
    
    opponent = {"A" : 1, "B": 2, "C" : 3}
    player = {"X" : 1, "Y": 2, "Z" : 3}

    if strategy:
        player_choice = use_strategy(opponent_choice, player_choice)
        
    player_score = player[player_choice]
    opponent_score = opponent[opponent_choice]

    # basic score for the shape
    score = player_score

    diff = player_score - opponent_score

    # draw
    if diff == 0:
        score += 3
    # win
    elif diff == 1 or diff == -2:
        score += 6

    return score           


def use_strategy(opponent_choice, round_end):
    """
    X means you need to lose,
    Y means you need to end the round in a draw,
    Z means you need to win.
    """

    # use the letters ASCI code of A, B, C to get indices 0, 1, 2
    # A is 65
    player_shapes = ["X", "Y", "Z"]

    # draw
    response = player_shapes[ord(opponent_choice) - 65]

    # loose
    if round_end == "X":
        response = player_shapes[ord(opponent_choice) - 66]

    # win
    elif round_end == "Z":
        response = player_shapes[(ord(opponent_choice) - 64) % 3]
        
    return response


if __name__ == "__main__":
    """
    advent of code day 2
    play rock-paper-scissors
    """
    filename = sys.argv[1]
    # filename = "advent02.txt"
    
    with open(filename, "r") as f:
        content = f.readlines()
        play_tournament(content)
        play_tournament(content, True)
