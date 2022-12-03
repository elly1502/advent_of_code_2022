# Day 3: Rucksack Reorganization
### Author: Helena L. Spiewak
### Date created: 2022-12-03

import os
import string


def parse_rucksack_items(input_items):
    """ Function that 
    :param input_items: Text file describing input items in rucksake 
    :return: c """

    with open(input_items, "r") as file:
        # counter
        rucksack_counts = {}
        rucksack_n = 1

        # read each line
        for rucksack in file:
            rucksack = rucksack.replace("\n", "")
            # split into two compartments
            num_items = len(rucksack)
            compartment_one = list(rucksack[0 : int(num_items / 2)])
            compartment_two = list(rucksack[int(num_items / 2) : num_items])
            # items that are in both
            in_both_comps = list(set(compartment_one).intersection(compartment_two))
            # total the priority of item
            count = 0
            for i in in_both_comps:
                try:
                    # lowercase
                    count += string.ascii_lowercase.index(i) + 1
                except ValueError:
                    # uppercase
                    count += string.ascii_uppercase.index(i) + 27
            # add to dict that is then returned
            rucksack_counts[rucksack_n] = count
            rucksack_n += 1
        return rucksack_counts


def group_rucksack_items(input_items):
    with open(input_items, "r") as file:
        # counter
        rucksack_counts = {}
        rucksack_n = 1
        elf_group = 0
        group = []
        # read each line
        for rucksack in file:
            rucksack = rucksack.replace("\n", "")
            # each line lines are an elf group
            if rucksack_n <= 3:
                # add rucksack to list
                group.append(rucksack)
                # summarise the elf group
                if rucksack_n == 3:
                    # define group
                    elf_group += 1
                    # find common
                    in_all = list(
                        set(group[0]).intersection(group[1]).intersection(group[2])
                    )
                    # total the priority of item
                    count = 0
                    for i in in_all:
                        try:
                            # lowercase
                            count += string.ascii_lowercase.index(i) + 1
                        except ValueError:
                            # uppercase
                            count += string.ascii_uppercase.index(i) + 27
                    # reset
                    rucksack_n = 0
                    group = []
                    rucksack_counts[elf_group] = count
                rucksack_n += 1
        return rucksack_counts


def sum_priority_items(rucksack_counts):
    """ Function that sums the priority counts in given dict.
    :param rucksack_counts: Dict of counts. 
    :return: Sum """
    return sum(rucksack_counts.values())


# unit tests
def create_test_file(input_items):
    # define filename
    test_file_path = "test_rucksack_items.txt"
    # remove temp test file
    try:
        os.remove(test_file_path)
    except:
        pass
    # write items to file
    with open(test_file_path, "w") as test:
        for rucksack in input_items:
            test.write("{}\n".format(rucksack))

    return test_file_path


def test_expected_read_rucksack_items():
    # create test text file
    input_items = create_test_file(
        [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
        ]
    )

    # test function
    assert parse_rucksack_items(input_items=input_items) == {1: 16, 2: 38, 3: 42}
    # remove file
    os.remove(input_items)


def test_expected_sum_priority_items():
    # test function
    assert sum_priority_items(rucksack_counts={1: 16, 2: 38, 3: 42}) == 96


def test_expected_group_rucksack_items():
    # create test text file
    input_items = create_test_file(
        [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
    )

    # test function
    assert group_rucksack_items(input_items=input_items) == {1: 18, 2: 52}
    # remove file
    os.remove(input_items)


# run the function on input
# puzzle 1
rucksack_counts = parse_rucksack_items(input_items="./input_day3.txt")
total_count = sum_priority_items(rucksack_counts=rucksack_counts)
print("Sum of the priorities = {}".format(total_count))

# puzzle 2
group_counts = group_rucksack_items(input_items="./input_day3.txt")
sum_prioritise_elf_group = sum_priority_items(rucksack_counts=group_counts)
print("Sum of the priorities for elf groups = {}".format(sum_prioritise_elf_group))
