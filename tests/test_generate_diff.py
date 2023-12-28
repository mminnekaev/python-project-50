import pytest
from gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/correct_answer1.txt', 'r') as f:
        correct_answer_1 = f.read()

    with open('tests/fixtures/correct_answer2.txt', 'r') as f:
        correct_answer_2 = f.read()

    with open('tests/fixtures/correct_answer_plain.txt', 'r') as f:
        correct_answer_plain = f.read()

    # check json input
    assert generate_diff(
        'tests/fixtures/file1_plain.json',
        'tests/fixtures/file2_plain.json'
    ) == correct_answer_1

    # check yml input
    assert generate_diff(
        'tests/fixtures/file1_plain.yml',
        'tests/fixtures/file2_plain.yml'
    ) == correct_answer_1

    # # check nested
    # assert generate_diff(
    #     'tests/fixtures/file1_nested.json',
    #     'tests/fixtures/file2_nested.json',
    #     format = 'stylish'
    # ) == correct_answer_2

    # check plain
    assert generate_diff(
        'tests/fixtures/file1_nested.json',
        'tests/fixtures/file2_nested.json',
        format='plain'
    ) == correct_answer_plain
