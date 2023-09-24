import json
import yaml


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


def generate_diff(file1, file2):
    data1, data2 = load_data(file1=file1, file2=file2)

    keys1 = list(data1.keys())
    keys1.sort()
    res = '{\n'

    for key in keys1:
        if data1.get(key) == data2.get(key):
            res = res + f'    {key}: {data1.get(key)}\n'
        elif data2.get(key) is None:
            res = res + f'  - {key}: {data1.get(key)}\n'
        else:
            res = res + f'  - {key}: {data1.get(key)}\n'
            res = res + f'  + {key}: {data2.get(key)}\n'

    keys2 = [key for key in list(data2.keys()) if key not in keys1]
    for key in keys2:
        res = res + f'  + {key}: {data2.get(key)}\n'

    res = res + '}'

    return res
