import json
import yaml
from ..formatters.stylish import stylish
from ..formatters.plain import plain


def load_data(file1, file2):
    if file1.split('.')[-1] == 'json':
        data1 = json.load(open(file1))
    elif file1.split('.')[-1] in {'yml', 'yaml'}:
        with open(file1, 'r') as yaml_file1:
            data1 = yaml.load(yaml_file1, Loader=yaml.FullLoader)

    if file2.split('.')[-1] == 'json':
        data2 = json.load(open(file2))
    elif file2.split('.')[-1] in {'yml', 'yaml'}:
        with open(file2, 'r') as yaml_file2:
            data2 = yaml.load(yaml_file2, Loader=yaml.FullLoader)

    return data1, data2


def make_inner_view(data1, data2):
    keys = sorted(list(data1.keys() | data2.keys()))
    res = list()

    for key in keys:
        if (key in data1) and (key in data2):
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
        elif key not in data2:
            res.append({
                'key': key,
                'value': data1[key],
                'meta': 'removed'
            })
        elif key not in data1:
            res.append({
                'key': key,
                'value': data2[key],
                'meta': 'added'
            })
    return res


def generate_diff(file1, file2, format='stylish'):
    data1, data2 = load_data(file1=file1, file2=file2)
    result_inner_view = make_inner_view(data1, data2)
    if format == 'stylish':
        return stylish(result_inner_view)
    if format == 'plain':
        return plain(result_inner_view)
