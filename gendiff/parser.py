import json
import yaml


def load_data(file):
    if file.split('.')[-1] == 'json':
        data = json.load(open(file))
    elif file.split('.')[-1] in {'yml', 'yaml'}:
        with open(file, 'r') as yaml_file:
            data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return data
