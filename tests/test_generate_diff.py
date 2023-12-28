import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
    "file1, file2, format, correct_result", [
        (
            'tests/fixtures/file1_plain.json',
            'tests/fixtures/file2_plain.json',
            'stylish',
            'tests/fixtures/correct_answer1.txt'
        ),
        (
            'tests/fixtures/file1_plain.yml',
            'tests/fixtures/file2_plain.yml',
            'stylish',
            'tests/fixtures/correct_answer1.txt'
        ),
        (
            'tests/fixtures/file1_nested.json',
            'tests/fixtures/file2_nested.json',
            'plain',
            'tests/fixtures/correct_answer_plain.txt'
        )
    ]
)
def test_generate_diff(file1, file2, format, correct_result):
    with open(correct_result) as f:
        result = f.read()
        diff = generate_diff(file1, file2, format=format)
        assert result == diff
