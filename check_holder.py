import json

with open("day1.json", "r") as file:
    data = json.loads(file.read())

i = 0
holder = {}

for i in range(0, len(data)):
    count = 1
    j = i + 1
    while j < len(data):
        if data[str(i)]["holder"] == data[str(j)]["holder"]:
            count += 1
        j += 1
    if not data[str(i)]["holder"] in holder.keys():
        holder[f"{data[str(i)]['holder']}"] = count
    # i += 1
print(holder)


with open("holder_day1.json", "w") as file:
    file.write(json.dumps(holder))

# str(j) in data.keys() and
