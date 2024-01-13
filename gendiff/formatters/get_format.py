from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json


def get_format(format):
    if format == 'stylish':
        return stylish
    if format == 'plain':
        return plain
    if format == 'json':
        return get_json
    raise ValueError('This format is not supported')
