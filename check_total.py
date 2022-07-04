import json

# with open("holder_to_date.json", "r") as file:
#     data = json.loads(file.read())
#     count = 0
#     for key in data:
#         print(data[key])
#         count += float(data[key])
#     print(count)

with open("holder_to_date.json", "r") as file:
    data = json.loads(file.read())
    count = 0
    for i in range(1, 4):
        for key in data[f"day{i}"]:
            print(data[f"day{i}"][key])
            count += float(data[f"day{i}"][key])
        print(count)
