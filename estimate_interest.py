import json

interest_per_nft_per_day = 100 / 30 / 200

interest = {}
with open("holder_day3.json", "r") as file:
    holders = json.loads(file.read())
    for key in holders:
        received_interest = holders[key] * interest_per_nft_per_day * 27
        print(received_interest)
        interest[key] = received_interest

with open("estimate_interest.json", "w") as file:
    file.write(json.dumps(interest))
