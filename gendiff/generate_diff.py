from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json
from gendiff.parser import load_data


# flake8: noqa: C901
def make_inner_view(data1, data2):
    res = list()
    all_keys = sorted(data1.keys() | data2.keys())
    added_keys = data2.keys() - data1.keys()
    removed_keys = data1.keys() - data2.keys()
    remained_keys = set(all_keys) - added_keys - removed_keys

    for key in all_keys:
        if key in remained_keys:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                res.append({
                    'key': key,
                    'value': make_inner_view(data1[key], data2[key]),
                    'meta': 'nested'
                })
            elif data1[key] != data2[key]:
                res.append({
                    'key': key,
                    'value': (data1[key], data2[key]),
                    'meta': 'changed'
                })
            elif data1.get(key) == data2.get(key):
                res.append({
                    'key': key,
                    'value': data1[key],
                    'meta': 'no difference'
                })
        elif key in removed_keys:
            res.append({
                'key': key,
                'value': data1[key],
                'meta': 'removed'
            })
        elif key in added_keys:
            res.append({
                'key': key,
                'value': data2[key],
                'meta': 'added'
            })
    return res


def generate_diff(file1, file2, format='stylish'):
    data1 = load_data(file1)
    data2 = load_data(file2)
    result_inner_view = make_inner_view(data1, data2)
    if format == 'stylish':
        return stylish(result_inner_view)
    if format == 'plain':
        return plain(result_inner_view)
    if format == 'json':
        return get_json(result_inner_view)
