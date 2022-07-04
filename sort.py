with open("snapshot_day1.txt", "r") as file:
    lines = file.readlines()
    lines.sort(key=lambda line: int(line.split("|")[0]))
# print(lines)
with open("snapshot_sorted.txt", "w") as file:
    file.writelines(lines)
token_ids = [int(x.split("|")[0]) for x in lines]
# print(token_ids)
# count = 0
# for i in range(0, 10001):
#     if i not in token_ids:
#         print(i)
#         count+=1
# print(count)
