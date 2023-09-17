import json


def generate_diff(file1, file2):
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    keys1 = list(file1.keys())
    keys1.sort()
    res = '{\n'

    for key in keys1:
        if file1.get(key) == file2.get(key):
            res = res + f'    {key}: {file1.get(key)}\n'
        elif file2.get(key) is None:
            res = res + f'  - {key}: {file1.get(key)}\n'
        else:
            res = res + f'  - {key}: {file1.get(key)}\n'
            res = res + f'  + {key}: {file2.get(key)}\n'

    keys2 = [key for key in list(file2.keys()) if key not in keys1]
    for key in keys2:
        res = res + f'  + {key}: {file2.get(key)}\n'

    res = res + '}'

    return res
