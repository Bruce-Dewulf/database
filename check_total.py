import json

with open("holder_day1.json", "r") as file:
    data = json.loads(file.read())
    count = 0
    for key in data:
        print(data[key])
        count += float(data[key])
    print(count)
