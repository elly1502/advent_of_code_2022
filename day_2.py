# Day 2: Calorie Counting
### Author: Helena L. Spiewak
### Date created: 2022-12-02

# Rock defeats Scissors, Scissors defeats Paper, 
# and Paper defeats Rock. If both players choose the same shape, 
# the round instead ends in a draw.

# dict of moves
opponent = {"A": "Rock", "B" : "Paper", "C": "Scissors"}
response = {"X": "Rock", "Y" : "Paper", "Z": "Scissors"}
scores = {"Rock": 1, "Paper": 2, "Scissors": 3}

def parse_strategy_guide(strategy_guide):
    with open(strategy_guide, "r") as file:
        for round in file:
            choices = round.replace("\n", "").split("\t")
            print(choices)
            if choices[0] == choices[1]:
                # draw
                

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


def test_expected_output_last():
    # create test text file
    strategy = create_test_file(["A\tY", "B\tX", "C\tZ"])

    # test function
    assert parse_strategy_guide(strategy_guide=strategy) == {1: 2200, 2: 110, 3: 10000}
    # remove file
    os.remove(strategy)