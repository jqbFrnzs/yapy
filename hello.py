from flask import Flask, render_template, request

from py_parser import PythonParser
from yml_parser import YamlParser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    py_parser = PythonParser()
    yml_parser = YamlParser()
    if request.method == 'POST':
        if 'yaml_to_python' in request.form: 
            code = request.form['yaml_to_python']
            yaml_output = py_parser.parse_to_yaml(code)
            return render_template('result.html', yaml_output=yaml_output)
        elif 'python_to_yaml' in request.form:
            code = request.form['python_to_yaml']
            yaml_output = yml_parser.parse_to_python(code)
            return render_template('result.html', yaml_output=yaml_output)
    return render_template('index.html')
