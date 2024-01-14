from gendiff.formatters.apply_format import apply_format
from gendiff.parser import get_data


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
        res.append({
            'key': key,
            'value': data1[key],
            'meta': 'no difference'
        })
    return res


def generate_diff(file1, file2, format='stylish'):
    data1 = get_data(file1)
    data2 = get_data(file2)
    result_inner_view = make_inner_view(data1, data2)
    result = apply_format(result_inner_view, format)
    return result
