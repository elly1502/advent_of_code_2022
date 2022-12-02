# Day 2: Rock Paper Scissors
### Author: Helena L. Spiewak
### Date created: 2022-12-02

import os

# dict of keys, scores and which defeats which
opponent = {"A": "Rock", "B": "Paper", "C": "Scissors"}
scores = {"Rock": 1, "Paper": 2, "Scissors": 3}
# key defeats value
defeats = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}


def per_round_score(strategy_guide):
    """ Function that takes a tab delimited text file which is a strategy guide:
    :param strategy_guide: Text file.
    :return: Dict of score for each round"""
    all_round_scores = {}
    with open(strategy_guide, "r") as file:
        # round counter
        round_n = 0
        # read each line
        for round in file:
            round_n += 1
            # reset score for each round
            round_score = 0
            shapes = round.replace("\n", "").split(" ")

            # get opponent shape
            opp_choice = opponent[shapes[0]]
            # get which outcome should happen
            outcome = shapes[1]

            # draw
            if outcome == "Y":
                # add outcome score
                round_score += 3
                # what shape is needed for this to happen
                your_choice = opp_choice
            # lose
            elif outcome == "X":
                round_score += 0
                your_choice = defeats[opp_choice]
            # win
            else:
                round_score += 6
                your_choice = [
                    key for key, val in defeats.items() if val == opp_choice
                ][0]

            # add choice score
            round_score += scores[your_choice]
            # add to dictionary
            all_round_scores[round_n] = round_score

        print("Score for rounds = {}".format(all_round_scores))

    return all_round_scores


def total_scores(all_round_scores):
    """ Function sum the individual round scores and return total.
    :param all_round_scores: Dict of integers:
    :return: Total of input Dict """
    return sum(all_round_scores.values())


# unit tests
def create_test_file(stategies):
    # define filename
    test_file_path = "test_strategy_guide.txt"
    # remove temp test file
    try:
        os.remove(test_file_path)
    except:
        pass
    # write calories to file
    with open(test_file_path, "w") as test:
        for strategy in stategies:
            test.write("{}\n".format(strategy))

    return test_file_path


def test_expected_output_per_round_score():
    # create test text file
    strategy = create_test_file(["A Y", "B X", "C Z"])

    # test function
    assert per_round_score(strategy_guide=strategy) == {1: 4, 2: 1, 3: 7}
    # remove file
    os.remove(strategy)


def test_total_scores():
    assert total_scores(all_round_scores={1: 4, 2: 1, 3: 7}) == 12


# run against input file
# parse input file
scores_per_round = per_round_score(strategy_guide="./input_day2.txt")
# puzzle 1
total = total_scores(scores_per_round)
print("Total score = {}".format(total))
