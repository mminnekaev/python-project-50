from json import dumps


INDENTS = {
    'added': '+ ',
    'removed': '- ',
    'no difference': '  ',
    'nested': '  '
}

BASE_INDENT = 4


def replace_dumps(value):
    if isinstance(value, bool) or value is None:
        return dumps(value)
    else:
        return value


def get_indent(meta, depth, symb=' '):
    if depth == 0:
        return ''
    elif depth > 0:
        indent = (BASE_INDENT * depth - 2) * symb + INDENTS.get(meta)
    return indent


def format_plain_dict(dictionary, depth=1):
    result = '{\n'
    for key in dictionary:
        if isinstance(dictionary[key], dict):
            result = result + f'{get_indent("nested", depth)}{key}: ' + \
                format_plain_dict(dictionary[key], depth + 1)
        else:
            result = result + f'{get_indent("nested", depth)}{key}: ' \
                              f'{replace_dumps(dictionary[key])}\n'
    result = result + get_indent("nested", depth - 1) + '}' + '\n'
    return result


def stylish(data, depth=1):
    result = '{\n'

    for elem in data:
        key = elem['key']
        value = elem['value']
        meta = elem['meta']

        if isinstance(value, list):
            result = result + f'{get_indent("nested", depth)}{key}: ' \
                              f'{stylish(value, depth + 1)}'
        elif not isinstance(value, dict):
            if meta == 'changed' and not isinstance(value[0], dict) \
                    and not isinstance(value[1], dict):
                result = result + f'{get_indent("removed", depth)}{key}: ' \
                                  f'{replace_dumps(value[0])}\n'
                result = result + f'{get_indent("added", depth)}{key}: ' \
                                  f'{replace_dumps(value[1])}\n'
            if meta == 'changed' and isinstance(value[0], dict):
                result = result + f'{get_indent("removed", depth)}{key}: ' \
                                  f'{format_plain_dict(value[0], depth + 1)}'
                result = result + f'{get_indent("added", depth)}{key}: ' \
                                  f'{replace_dumps(value[1])}\n'
            if meta == 'changed' and isinstance(value[1], dict):
                result = result + f'{get_indent("removed", depth)}{key}: ' \
                                  f'{replace_dumps(value[0])}\n'
                result = result + f'{get_indent("added", depth)}{key}: ' \
                                  f'{format_plain_dict(value[1], depth + 1)}'
            elif meta in ('added', 'removed', 'no difference'):
                result = result + f'{get_indent(meta, depth)}{key}: ' \
                                  f'{replace_dumps(value)}\n'
        elif isinstance(value, dict):
            if meta in ('added', 'removed', 'no difference'):
                result = result + f'{get_indent(meta, depth)}{key}: ' \
                                  f'{format_plain_dict(value, depth + 1)}'
            elif meta == 'nested':
                result = result + f'{get_indent("nested", depth)}{key}: ' \
                                  f'{stylish(value, depth + 1)}'

    result = result + get_indent('nested', depth - 1) + '}\n'

    if depth != 1:
        return result
    else:
        return result[:-1]
