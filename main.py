def parse_yaml(yaml_string):
    yaml_lines = yaml_string.strip().split('\n')
    data = {}
    indent_level = 0
    for line in yaml_lines:
        if line.strip() == '':
            continue
        line_indent_level = len(line) - len(line.lstrip())
        if line_indent_level == 0:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
        elif line_indent_level > indent_level:
            if not isinstance(data[key], dict):
                data[key] = {}
            sub_key, sub_value = line.split(':', 1)
            data[key][sub_key.strip()] = sub_value.strip()
        else:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
        indent_level = line_indent_level
    return data

def serialize_yaml(data, indent=0):
    yaml_string = ''
    for key, value in data.items():
        if isinstance(value, dict):
            yaml_string += ' ' * indent + key + ':\n'
            yaml_string += serialize_yaml(value, indent=indent+2)
        else:
            yaml_string += ' ' * indent + key + ': ' + str(value) + '\n'
    return yaml_string

yaml_string = '''
name: John
age: 30
address:
  street: Main St.
  city: New York
'''
data = parse_yaml(yaml_string)
print(data)
# Output: {'name': 'John', 'age': '30', 'address': {'street': 'Main St.', 'city': 'New York'}}

data['address']['zip'] = 10001
yaml_string = serialize_yaml(data)
print(yaml_string)
# Output: 
# name: John
# age: 30
# address:
#   street: Main St.
#   city: New York
#   zip: 10001

