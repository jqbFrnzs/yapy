import ast
from flask import Flask, render_template, request
import yaml

def parse_to_yaml(code):
    # Parse the Python code to YAML using the desired logic/library
    # For example, using the `yaml` module:
    yaml_string = code
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
    yaml_output = data
    return yaml_output

def parse_to_python(data):
    data = eval(data)
    try:
        yaml_string = yaml.dump(data)
        return yaml_string
    except yaml.YAMLError as e:
        print("Error converting to YAML:", str(e))
        return None

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'yaml_to_python' in request.form: 
            code = request.form['yaml_to_python']
            yaml_output = parse_to_yaml(code)
            return render_template('result.html', yaml_output=yaml_output)
        elif 'python_to_yaml' in request.form:
            code = request.form['python_to_yaml']
            yaml_output = parse_to_python(code)
            return render_template('result.html', yaml_output=yaml_output)
    return render_template('index.html')
