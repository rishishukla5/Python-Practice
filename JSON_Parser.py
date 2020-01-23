import json

read_file = open("quiz.json", "r", encoding="utf-8")
data = json.load(read_file)
read_file.close()
print(data['quiz'])
