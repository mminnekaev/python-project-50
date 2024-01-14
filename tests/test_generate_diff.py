import pytest
from gendiff import generate_diff

FIXTURES_DIR = 'tests/fixtures/'

@pytest.mark.parametrize(
    "file1, file2, format, correct_result", [
        (
            'file1_plain.json',
            'file2_plain.json',
            'stylish',
            'correct_answer1.txt'
        ),
        (
            'file1_plain.yml',
            'file2_plain.yml',
            'stylish',
            'correct_answer1.txt'
        ),
        (
            'file1_nested.json',
            'file2_nested.json',
            'plain',
            'correct_answer_plain.txt'
        )
    ]
)
def test_generate_diff(file1, file2, format, correct_result):
    with open(FIXTURES_DIR + correct_result) as f:
        result = f.read()
        diff = generate_diff(
            FIXTURES_DIR + file1,
            FIXTURES_DIR + file2,
            format=format
        )
        assert result == diff
