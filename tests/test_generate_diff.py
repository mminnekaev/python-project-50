import pytest
from gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/correct_answer1') as f:
        correct_answer = f.read()

    # check json input
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    ) == correct_answer

    # check yml input
    assert generate_diff(
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml'
    ) == correct_answer

