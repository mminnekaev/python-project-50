def format_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, tuple):
        return (format_value(value[0]), format_value(value[1]))
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

        if meta == 'added' and isinstance(value, dict):
            result.append(f"Property '{node}{key}' was added "
                          f"with value: [complex value]")
        elif meta == 'added':
            result.append(f"Property '{node}{key}' was added "
                          f"with value: {value}")
        elif meta == 'removed':
            result.append(f"Property '{node}{key}' was removed")
        elif meta == 'changed' and not isinstance(value[0], dict) \
                and not isinstance(value[1], dict):
            result.append(f"Property '{node}{key}' was updated. "
                          f"From {value[0]} to {value[1]}")
        elif meta == 'changed' and isinstance(value[0], dict):
            result.append(f"Property '{node}{key}' was updated. "
                          f"From [complex value] to {value[1]}")
        elif meta == 'changed' and isinstance(value[1], dict):
            result.append(f"Property '{node}{key}' was updated. "
                          f"From {value[0]} to [complex value]")
        elif meta == 'nested':
            result.append(plain(value, node=node + key + '.'))

    return '\n'.join(result)
