INDENTS = {
    'added': '+ ',
    'removed': '- ',
    'no difference': '  ',
    'nested': '  '
}

BASE_INDENT = 4


def get_indent(meta, depth, symb=' '):
    if depth == 0:
        return ''
    elif depth > 0:
        indent = (BASE_INDENT * depth - 2) * symb + INDENTS.get(meta)
    return indent


def format_values(value, depth=1):
    if isinstance(value, dict):
        result = ['{']
        for key in value:
            if isinstance(value[key], dict):
                result.append(f'{get_indent("nested", depth)}{key}: '
                              f'{format_values(value[key], depth + 1)}')
            else:
                result.append(f'{get_indent("nested", depth)}{key}: '
                              f'{format_values(value[key])}')
        result.append(get_indent("nested", depth - 1) + '}')
        return '\n'.join(result)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def stylish(data, depth=1):
    result = ['{']
    for elem in data:
        key = elem['key']
        value = elem['value']
        meta = elem['meta']

        # nested result
        if meta == 'nested':
            result.append(f'{get_indent("nested", depth)}{key}: '
                          f'{stylish(value, depth + 1)}')
        # value is dict
        elif meta in ('added', 'removed', 'no difference') \
                and isinstance(value, dict):
            result.append(f'{get_indent(meta, depth)}{key}: '
                          f'{format_values(value, depth + 1)}')
        # value is tuple
        elif meta == 'changed':
            result.append(f'{get_indent("removed", depth)}{key}: '
                          f'{format_values(value[0], depth + 1)}')
            result.append(f'{get_indent("added", depth)}{key}: '
                          f'{format_values(value[1], depth + 1)}')
        elif meta in ('added', 'removed', 'no difference'):
            result.append(f'{get_indent(meta, depth)}{key}: '
                          f'{format_values(value)}')

    result.append(get_indent('nested', depth - 1) + '}')

    return '\n'.join(result)
