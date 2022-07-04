import json

holder = {}
for a in range(1, 4):
    with open(f"day{a}.json", "r") as file:
        data = json.loads(file.read())

    holder[f"day{a}"] = {}

    for i in range(0, len(data)):
        count = 1
        j = i + 1
        while j < len(data):
            if data[str(i)]["holder"] == data[str(j)]["holder"]:
                count += 1
            j += 1
        if not data[str(i)]["holder"] in holder[f"day{a}"].keys():
            holder[f"day{a}"][f"{data[str(i)]['holder']}"] = count
    print(holder)


with open("holder_to_date.json", "w") as file:
    file.write(json.dumps(holder))
