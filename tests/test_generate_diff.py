import pytest
from gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/correct_answer1.txt', 'r') as f:
        correct_answer_1 = f.read()

    with open('tests/fixtures/correct_answer2.txt', 'r') as f:
        correct_answer_2 = f.read()

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

    # check nested
    assert generate_diff(
        'tests/fixtures/file1_nested.json',
        'tests/fixtures/file2_nested.json'
    ) == correct_answer_2
