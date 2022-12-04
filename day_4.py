# Day 4: Camp Cleanup
### Author: Helena L. Spiewak
### Date created: 2022-12-04

import os
import csv


def overlapping_assignment_pairs(section_assignments, overlap_type="all"):
    """ Function that finds elf pairs that have overlapping assignments given
    a section assignment text file as input.
    :param section_assignments: Text file containingg section assignment pairs.
    :param overlap_type: Type of overlap. Default is all.
    :return: Number of elf-pairs with overlapping assignment as a list. """
    # read in assignment pairs
    with open(section_assignments, "r") as file:
        assignment_reader = csv.reader(file, delimiter=",")
        # counter
        elf_pair_n = 0
        overlap = []
        for row in assignment_reader:
            # increment counter
            elf_pair_n += 1
            # parse into a list of lists
            assignment_pair = [
                list(range(int(i.split("-")[0]), int(i.split("-")[1]) + 1)) for i in row
            ]
            # compare assignments
            if overlap_type == "all":
                check_one = all(
                    item in assignment_pair[0] for item in assignment_pair[1]
                )
                check_two = all(
                    item in assignment_pair[1] for item in assignment_pair[0]
                )
            elif overlap_type == "any":
                check_one = any(
                    item in assignment_pair[0] for item in assignment_pair[1]
                )
                check_two = any(
                    item in assignment_pair[1] for item in assignment_pair[0]
                )

            # add to output if they overlap
            if check_one or check_two:
                overlap.append(elf_pair_n)

    return overlap


def count_overlap(overlap):
    """ Function to count number of overlapping elf pairs"""
    return len(overlap)


# unit tests
def create_test_file(input_items):
    # define filename
    test_file_path = "test_section_assignments.txt"
    # remove temp test file
    try:
        os.remove(test_file_path)
    except:
        pass
    # write items to file
    with open(test_file_path, "w") as test:
        for section_assignment in input_items:
            test.write("{}\n".format(section_assignment))

    return test_file_path


def test_expected_overlapping_assignment_pairs_all():
    # create test text file
    section_assignments = create_test_file(
        ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8",]
    )

    # test function
    assert overlapping_assignment_pairs(
        section_assignments=section_assignments, overlap_type="all"
    ) == [4, 5,]
    # remove file
    os.remove(section_assignments)


def test_expected_count_overlap():
    assert count_overlap([4, 5]) == 2


def test_expected_overlapping_assignment_pairs_any():
    # create test text file
    section_assignments = create_test_file(
        ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8",]
    )

    # test function
    assert overlapping_assignment_pairs(
        section_assignments=section_assignments, overlap_type="any"
    ) == [3, 4, 5, 6]
    # remove file
    os.remove(section_assignments)


# run functions on input file
# puzzle 1
overlaps = overlapping_assignment_pairs(section_assignments="./input_day4.txt")
count = count_overlap(overlap=overlaps)
print("Number of elf pairs with all overlapping assignments = {}".format(count))

# puzzle 2
overlaps = overlapping_assignment_pairs(
    section_assignments="./input_day4.txt", overlap_type="any"
)
count = count_overlap(overlap=overlaps)
print("Number of elf pairs with any overlapping assignments = {}".format(count))
