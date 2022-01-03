import json

PRE_SHEET = '\\version "2.22.1" \n \score{\n {\n  \key des \major \n'
POST_SHEET = '}\n  \layout{ }\n  \midi { \\tempo 4=100 }\n}'

PRE_TAB = '\\new TabStaff{ \n \\tabFullNotation \n'
POST_TAB = '} \n '

def read_key_file(filename):
        data = []
        with open(filename, 'r') as file:
                data = file.read()
        return json.loads(data)

def write_key_file(filename, confDict):
        json_obj = json.dumps(confDict, indent=4)
        with open(filename, 'w') as file:
                file.write(json_obj)

def write_sheet(file, notes, sheet):
        print("SHEET: " + str(type(sheet)))   
        file.write(PRE_SHEET)
        if(sheet == "1"): 
            file.write(PRE_TAB)
        file.writelines(notes)
        if(sheet == "1"): 
            file.write(POST_TAB)
        file.write(POST_SHEET)
            
        