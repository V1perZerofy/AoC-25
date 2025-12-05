with open("inputs/input3.txt") as f:
    lines = f.read().strip().split("\n")

res = 0
for line in lines:
    highest = 0
    for i in range(len(line)):
        for j in range(len(line[i:]) - 1):
            #print(line[i], line[i + j + 1])
            if int(line[i] + line[i + j + 1]) > highest:
                highest = int(line[i] + line[i + j + 1])
    res += highest
    #print(highest)

res2 = 0

for line in lines:
    num = []
    last = 0
    while len(num) < 12:
        highest2 = -1
        bestIdx = -1
        for i in range(len(line)):
            idx = last + i
            if (12 - len(num) - 1) <= (len(line) - idx - 1):
                if int(line[idx]) > highest2:
                    highest2 = int(line[idx])
                    bestIdx = idx
        num.append(highest2)
        last = bestIdx + 1
    print(num)
    res2 += int("".join(str(i) for i in num))

print(res2)
