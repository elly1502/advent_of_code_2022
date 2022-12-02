# Day 1: Calorie Counting
### Author: Helena L. Spiewak
### Date created: 2022-12-01

import os
import operator


def count_inventory(inventory):
    """ Function that takes a inventory list of integers that 
    describes the number of calories elves are carry, and returns total for each elf. 
    :param inventory: Text file with calories for each elf in.
    :return: Dict with total calories that each elf is carrying """
    # parse inventory file
    calorie_count = 0
    elf_count = 1
    # starting count dict
    elves = {elf_count: calorie_count}
    with open(inventory, "r") as file:
        for snack in file:
            if snack != "\n":
                # add calories together
                calorie_count += int(snack)
                elves[elf_count] = calorie_count
            # blank line seperate elves
            else:
                # reset
                calorie_count = 0
                elf_count += 1
    # return dict
    return elves


def calorific_elf(elves):
    """ Function that takes a dict that 
    describes the number of calories Elves are carry, and returns the Elf carrying 
    the most calories and their total. 
    :param elves: Dictionary of calorie count for each elf.
    :return: tuple of elf number and total calories the elf is carrying """

    # postion and total of the elf with most calories
    greedy_elf = max(elves, key=elves.get)
    most_calories = max(elves.values())

    print(
        "Elf carrying most calories is Elf {}, with {} total calories!".format(
            greedy_elf, most_calories
        )
    )
    # return as tuple
    return (greedy_elf, most_calories)


def top_x_elves(elves, x):
    """ Function that takes a dict that
    describes the number of calories Elves are carry, and top x elves and total of these.
    :param elves: Dictionary of calorie count for each elf.
    :param x: Top x elves
    :return: Dict of top x elves and total calories of these. """
    # calculate x number of elves with most calories
    top_elves = sorted(elves.items(), key=operator.itemgetter(1), reverse=True)[0:x]
    # summise calories of top eleves
    total = 0
    for elf, t in top_elves:
        total += t
    print("Top {} elves are: {}, with total calories: {}!".format(x, top_elves, total))

    # return as dict
    return {"elves": top_elves, "total": total}


# unit tests
def create_test_file(calories):
    # define filename
    test_file_path = "test_inventory.txt"
    # remove temp test file
    try:
        os.remove(test_file_path)
    except:
        pass
    # write calories to file
    with open(test_file_path, "w") as test:
        for snack in calories:
            test.write("{}\n".format(snack))

    return test_file_path


def test_expected_output_last():
    # create test text file
    inventory = create_test_file([1000, 1200, "", 20, 40, 50, "", 10000])

    # test function
    assert count_inventory(inventory=inventory) == {1: 2200, 2: 110, 3: 10000}
    # remove file
    os.remove(inventory)


def test_expected_output_calorific_elf_first():
    # test function
    assert calorific_elf(elves={1: 100, 2: 300, 3: 400}) == (3, 400)


def test_top_elves():
    assert top_x_elves(elves={1: 100, 2: 300, 3: 400, 4: 2}, x=3) == {
        "elves": [(3, 400), (2, 300), (1, 100)],
        "total": 800,
    }


# run against input file
# parse input file
inventory = count_inventory(inventory="./input_day1.txt")
# puzzle 1
calorific_elf(inventory)
# puzzle 2
top_x_elves(inventory, x=3)
