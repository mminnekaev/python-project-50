import json
import yaml


def parse(data, format):
    if format in {'yml', 'yaml'}:
        return yaml.load(data, Loader=yaml.FullLoader)
    elif format == 'json':
        return json.loads(data)
    raise ValueError("This data format is not supported")


def load_data(path):
    format = path.split('.')[-1]
    with open(path) as f:
        data = f.read()
    return parse(data, format)
