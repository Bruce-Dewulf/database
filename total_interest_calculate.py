import json

with open("received_interest.json", "r") as file:
    received_interest_holders = json.loads(file.read())

with open("estimate_interest.json", "r") as file:
    estimate_interest_holders = json.loads(file.read())

total_interest = received_interest_holders
for key in estimate_interest_holders:
    if key in received_interest_holders.keys():
        total_interest[key] += estimate_interest_holders[key]
        print(total_interest[key])

with open("total_interest.json", "w") as file:
    file.write(json.dumps(total_interest))
