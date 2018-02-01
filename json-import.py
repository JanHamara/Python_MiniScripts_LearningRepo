#! /usr/bin/env python
""" json-import.py, by Jan Hamara, 2018-01-10

    This script uses json module to execute conversion between string and object data structure
"""

import json

def add_employee(salaries_json, name, salary):
    file_json = json.loads(salaries_json)
    try:
    	file_json[str(name)] = int(salary)
    except ValueError:
    	print("Make sure your input values are correct")
    salaries_json = json.dumps(file_json)

    return salaries_json

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", "sup")
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])