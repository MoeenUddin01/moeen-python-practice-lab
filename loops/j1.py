import json

user = {"id": 23394, "username": "Moeen", "role": "Ai Engineer"}

json_data = json.dumps(user)
print(json_data)
print(type(json_data))
