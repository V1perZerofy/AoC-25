with open("inputs/input6.txt") as f:
    lines = f.read().strip().split("\n")

lines = [i.split(" ") for i in lines]

cleaned = [
    [item for item in row if item.strip() != ""]
    for row in lines
]

res = 0
for i in range(len(cleaned[0])):
    num = 0
    operator = cleaned[-1][i]
    for j in range(len(cleaned) - 1):
        if num == 0 and operator == "*":
            num = int(cleaned[j][i])
        elif operator == "*":
            num *= int(cleaned[j][i])
        else:
            num += int(cleaned[j][i])
    res += num

print(res)

