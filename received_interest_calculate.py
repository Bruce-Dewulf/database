import json

interest_per_nft_per_day = 100 / 30 / 200
print(interest_per_nft_per_day)


interest = {}
with open("today_holders_count.json", "r") as file:
    holders = json.loads(file.read())
    for key in holders:
        received_interest = holders[key] * interest_per_nft_per_day
        print(received_interest)
        interest[key] = received_interest

with open("received_interest.json", "w") as file:
    file.write(json.dumps(interest))
