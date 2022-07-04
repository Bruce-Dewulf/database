import json

with open("snapshot_day1.txt", "r") as file:
    lines = file.readlines()
    data = {}
    for i in range(0, len(lines)):
        data[i] = {
            "tokenId": lines[i].split("|")[0],
            "holder": lines[i].split("|")[1].replace("\n", ""),
        }
with open("day1.json", "w") as file:
    file.write(json.dumps(data))
