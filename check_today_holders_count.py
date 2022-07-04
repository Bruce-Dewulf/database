import json

with open("holder_to_date.json", "r") as file:
    holders = json.loads(file.read())

holders_data = holders["day1"]
for i in range(2, 4):
    for key in holders[f"day{i}"]:
        if key in holders_data.keys():
            holders_data[key] += holders[f"day{i}"][key]
        else:
            holders_data.update({key: holders[f"day{i}"][key]})
            print({key: holders[f"day{i}"][key]})

with open("today_holders_count.json", "w") as file:
    file.write(json.dumps(holders_data))
