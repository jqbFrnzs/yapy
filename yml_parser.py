import yaml

class YamlParser:
    
    def __init__(self):
        pass
    
    def parse_to_python(self, data):
        data = eval(data)
        try:
            yaml_string = yaml.dump(data)
            return yaml_string
        except yaml.YAMLError as e:
            print("Error converting to YAML:", str(e))
            return None
