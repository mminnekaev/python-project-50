from gendiff.formatters.get_format import get_format
from gendiff.parser import load_data


def make_inner_view(data1, data2):
    res = list()
    all_keys = sorted(data1.keys() | data2.keys())
    added_keys = data2.keys() - data1.keys()
    removed_keys = data1.keys() - data2.keys()

    for key in all_keys:
        if key in added_keys:
            res.append({
                'key': key,
                'value': data2[key],
                'meta': 'added'
            })
            continue
        if key in removed_keys:
            res.append({
                'key': key,
                'value': data1[key],
                'meta': 'removed'
            })
            continue
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            res.append({
                'key': key,
                'value': make_inner_view(data1[key], data2[key]),
                'meta': 'nested'
            })
            continue
        if data1[key] != data2[key]:
            res.append({
                'key': key,
                'value': (data1[key], data2[key]),
                'meta': 'changed'
            })
            continue
        if data1.get(key) == data2.get(key):
            res.append({
                'key': key,
                'value': data1[key],
                'meta': 'no difference'
            })
    return res


def generate_diff(file1, file2, format='stylish'):
    data1 = load_data(file1)
    data2 = load_data(file2)
    result_inner_view = make_inner_view(data1, data2)
    formatter = get_format(format)
    result = formatter(result_inner_view)
    return result
