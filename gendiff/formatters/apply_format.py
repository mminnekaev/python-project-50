from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json


def apply_format(content, format):
    if format == 'stylish':
        return stylish(content)
    if format == 'plain':
        return plain(content)
    if format == 'json':
        return get_json(content)
    raise ValueError('This format is not supported')
