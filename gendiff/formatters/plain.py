from json import dumps


def format_value(value):
    if isinstance(value, bool) or value is None:
        return dumps(value)
    elif isinstance(value, tuple):
        return (format_value(value[0]), format_value(value[1]))
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def plain(data, node=''):
    result = ''
    for elem in data:
        key = elem['key']
        value = format_value(elem['value'])
        meta = elem['meta']

        if meta == 'added':
            if isinstance(value, dict):
                result = result + f"Property '{node}{key}' was added " \
                                  f"with value: [complex value]\n"
            else:
                result = result + f"Property '{node}{key}' was added " \
                                  f"with value: {value}\n"
        elif meta == 'removed':
            result = result + f"Property '{node}{key}' was removed\n"
        elif meta == 'changed':
            if not isinstance(value[0], dict) \
                    and not isinstance(value[1], dict):
                result = result + f"Property '{node}{key}' was updated. " \
                                  f"From {value[0]} to {value[1]}\n"
            elif isinstance(value[0], dict):
                result = result + f"Property '{node}{key}' was updated. " \
                                  f"From [complex value] to {value[1]}\n"
            elif isinstance(value[1], dict):
                result = result + f"Property '{node}{key}' was updated. " \
                                  f"From {value[0]} to [complex value]\n"
        elif meta == 'nested':
            result = result + plain(value, node=node + key + '.')

    return result
