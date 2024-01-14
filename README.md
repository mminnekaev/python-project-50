### Hexlet tests and linter status:
[![Actions Status](https://github.com/mminnekaev/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/mminnekaev/python-project-50/actions)
[![Tests](https://github.com/mminnekaev/python-project-50/workflows/Python%20CI/badge.svg)](https://github.com/mminnekaev/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/b1fa8193364795606d7f/maintainability)](https://codeclimate.com/github/mminnekaev/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b1fa8193364795606d7f/test_coverage)](https://codeclimate.com/github/mminnekaev/python-project-50/test_coverage)

### Description:
The utility calculates the difference between two config files.

- Input: 2 file in _json_ or _yaml_ formats
- Optional input: format type (_--format_ parameter). Options are **plain**, **stylish** or **json**.
- Output: result file in _plain text_, _stylish_ or _json_ format

### How to install:
```
git clone git@github.com:mminnekaev/python-project-50.git
cd python-project-50/
install poetry
make install
```

### Usage examples:
```
# Help on the utility
gendiff help

# Make diff of two files in default format
gendiff file1 file2

# Make diff of two files in default format
gendiff file1 file2 --format [plain/json/stylish]
```

### Demonstration:
<a href=https://asciinema.org/a/SBREcOTQILx6m0Bz46887swwM><img src="https://asciinema.org/a/SBREcOTQILx6m0Bz46887swwM.svg"></a>
