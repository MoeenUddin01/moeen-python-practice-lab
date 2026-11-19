import json

employees = [
    {"id": 1, "name": "Moeen", "department": "AI"},
    {"id": 2, "name": "Ali", "department": "Backend"},
    {"id": 3, "name": "Ahmed", "department": "DevOps"},
]


for emplyess in employees:
    print(emplyess["name"])

json_data = json.dumps(employees)

print(json_data)
print(type(json_data))

pthon_data = json.loads(json_data)
print(pthon_data)
print(type(pthon_data))
