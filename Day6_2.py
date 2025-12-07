import re

with open("inputs/input6.txt") as f:
    lines = f.read().strip().split("\n")

operator = re.findall(r".", lines[-1])
nums = [re.findall(r".", lines[i]) for i in range(len(lines) - 1)]

start, end = 0, 0
allPairs = []
for idx, op in enumerate(operator[:-1]):
    current = []
    if operator[idx + 1] == "+" or operator[idx + 1] == "*":
        end = idx
        for line in range(len(nums)):
            current.append(nums[line][start:end][::-1])
        allPairs.append(current)
        start = idx + 1

current = []
for line in range(len(nums)):
    current.append(nums[line][start:len(nums[line])][::-1])
allPairs.append(current)

operator = [
    item for item in operator if item.strip() != ""
]

print(operator)
print(len(operator), len(allPairs))

res = 0
for idx, i in enumerate(allPairs):
    resT = 0
    op = operator[idx]
    for j in range(len(i[0])):
        num = ""
        for e in i:
            num += e[j]
        if resT == 0:
            resT = int(num)
        elif op == "*":
            resT *= int(num)
        else:
            resT += int(num)
    res += resT

print(res)
