import json

def read_key_file(filename):
        data = []
        with open(filename, 'r') as file:
                data = file.read()
        return json.loads(data)

def write_key_file(filename, confDict):
        json_obj = json.dumps(confDict, indent=4)
        with open(filename, 'w') as file:
                file.write(json_obj)

