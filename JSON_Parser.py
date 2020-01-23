import json

read_file = open("quiz.json", "r", encoding="utf-8")
data = json.load(read_file)
read_file.close()
json.dump(data, open("output.json", "w"), indent=4, sort_keys=True)
json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
parsed_json = json.loads(json_data)
print(json.dumps(parsed_json, indent=4, sort_keys=True))
