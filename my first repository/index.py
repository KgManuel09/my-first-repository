import json

with open("example.json", "r") as json_file:
    a = json.load(json_file)

del a["Media"]["Like"]

a["Mass"] = [1, "b", {"b": 2}, [1, 2, 3]]

print(json.dumps(a, indent=2))

with open("example.json", "w") as json_file:
    json.dump(a, json_file, indent=4)
