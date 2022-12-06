# Day 5: Supply Stacks
### Author: Helena L. Spiewak
### Date created: 2022-12-06

import os
import csv
import re


def parse_starting_crate_stacks(input):
    """ Function that takes starting crate stacks from input and converts into a dictionary.
    :param input: Text file containing start stack input.
    :return: Starting crate stacks as a dict of lists. """
    stack_dict = {}
    # read in input
    with open(input, "r") as file:
        # read read line
        for row in file:
            row = row.replace("\n", "")
            # end at
            if "1" in row:
                break
            else:
                # split the row into a list
                split_row = re.split(r"\s{1,4}", row)
                print(split_row)
                for index, crate in enumerate(split_row):
                    if crate != "":
                        try:
                            stack_dict[index + 1].append(crate)
                        except KeyError:
                            stack_dict[index + 1] = [crate]
    # remove
    # print(stack_dict)
    return stack_dict


def parse_moves(input):
    """ Function that takes moves from input and converts into a list.
    :param input: Text file containing starting stacks and moves.
    :return: Moves as a list. """
    move_list = []
    # read in input
    with open(input, "r") as file:
        # read read line
        for row in file:
            row = row.replace("\n", "").split(" ")
            # end at
            if "move" in row:
                move_list.append(row)
    # print(move_list)
    return move_list


def move_stacks_top(stacks_dict, move_list, move_type="individual"):
    """ Function to move in starting stacks based on given moves and return top crate
    on each stack.
    :param stacks_dict: Starting stack plan dictionary.
    :param move_list: List of moves.
    :param move_type: Move type based on crane type. Default is individual.
    :return: Top create on each stack as a string"""
    # loop through moves
    for instruction in move_list:
        move_n = int(instruction[1])
        from_stack = stacks_dict[int(instruction[3])][0:move_n]
        print(from_stack)
        # remove stack
        stacks_dict[int(instruction[3])] = stacks_dict[int(instruction[3])][move_n:]
        # add stack
        stacks_dict[int(instruction[5])] = from_stack + stacks_dict[int(instruction[5])]

    print(stacks_dict)
    # get the top crate in each stack
    top_crates = "".join(
        [re.sub(r"\[|\]", "", stacks_dict[i][0]) for i in sorted(stacks_dict.keys())]
    )
    return top_crates


# unit tests
def create_test_file(input_items):
    # define filename
    test_file_path = "test_stacks.txt"
    # remove temp test file
    try:
        os.remove(test_file_path)
    except:
        pass
    # write items to file
    with open(test_file_path, "w") as test:
        for stack in input_items:
            test.write("{}\n".format(stack))

    return test_file_path


# define test data
input_items = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]


def test_expected_parse_starting_crate_stacks():
    # create test text file
    stacks = create_test_file(input_items)

    # test function
    assert parse_starting_crate_stacks(input=stacks) == {
        1: ["[N]", "[Z]"],
        2: ["[D]", "[C]", "[M]"],
        3: ["[P]"],
    }
    # remove file
    os.remove(stacks)


def test_expected_parse_moves():
    # create test text file
    stacks = create_test_file(input_items)

    # test function
    assert parse_moves(input=stacks) == [
        ["move", "1", "from", "2", "to", "1"],
        ["move", "3", "from", "1", "to", "3"],
        ["move", "2", "from", "2", "to", "1"],
        ["move", "1", "from", "1", "to", "2"],
    ]
    # remove file
    os.remove(stacks)


def test_expected_move_stacks():
    # create test text file
    assert (
        move_stacks_top(
            stacks_dict={1: ["[N]", "[Z]"], 2: ["[D]", "[C]", "[M]"], 3: ["[P]"],},
            move_list=[
                ["move", "1", "from", "2", "to", "1"],
                ["move", "3", "from", "1", "to", "3"],
                ["move", "2", "from", "2", "to", "1"],
                ["move", "1", "from", "1", "to", "2"],
            ],
            move_type="multiple",
        )
        == "MCD"
    )


# run function for each puzzle
# puzzle 1
stacks_dict = parse_starting_crate_stacks(input="./input_day5.txt")
print(stacks_dict)
move_list = parse_moves(input="./input_day5.txt")
top_stacks = move_stacks_top(stacks_dict=stacks_dict, move_list=move_list)
print("Top stacks = {}".format(top_stacks))
