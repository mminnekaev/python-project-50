def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, tuple):
        return (format_value(value[0]), format_value(value[1]))
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def plain(data, node=''):
    result = []
    for elem in data:
        key = elem['key']
        value = format_value(elem['value'])
        meta = elem['meta']

        if meta == 'added':
            result.append(f"Property '{node}{key}' was added "
                          f"with value: {value}")
        elif meta == 'removed':
            result.append(f"Property '{node}{key}' was removed")
        elif meta == 'changed':
            result.append(f"Property '{node}{key}' was updated. "
                          f"From {value[0]} to {value[1]}")
        elif meta == 'nested':
            result.append(plain(value, node=node + key + '.'))

    return '\n'.join(result)
