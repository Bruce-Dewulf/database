import json

interest_per_nft_per_day = 100 / 30 / 200
print(interest_per_nft_per_day)


with open("holder_day1.json", "r") as file:
    holders_day1 = json.loads(file.read())
with open("holder_day2.json", "r") as file:
    holders_day2 = json.loads(file.read())
with open("holder_day3.json", "r") as file:
    holders_day3 = json.loads(file.read())


# holders = holders_day1
# for key in holders_day2:
#     if key in holders.keys():
#         holders[key] += holders_day2[key]
#     else:
#         holders.update({key: holders_day2[key]})
#         print({key: holders_day2[key]})
# for key in holders_day3:
#     if key in holders.keys():
#         holders[key] += holders_day3[key]
#     else:
#         holders.update({key: holders_day3[key]})
#         print({key: holders_day3[key]})
# with open("today_holders_count.json", "w") as file:
#     file.write(json.dumps(holders))
interest = {}
with open("today_holders_count.json", "r") as file:
    holders = json.loads(file.read())
    for key in holders:
        received_interest = holders[key] * interest_per_nft_per_day
        print(received_interest)
        interest[key] = received_interest

with open("received_interest.json", "w") as file:
    file.write(json.dumps(interest))
