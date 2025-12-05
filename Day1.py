with open("inputs/input1.txt") as f:
    lines = f.read().strip().split("\n")

dial = 50
res2 = 0
res1 = 0
for line in lines:
    num = int(line[1:])
    for i in range(num):
        if line[0] == "R":
            dial += 1
        else:
            dial -= 1


        if dial == 100:
            dial = 0
        elif dial == -1:
            dial = 99

        if dial == 0:
            res2 += 1

    if dial == 0:
        res1 += 1




print("res1: " + str(res1))
print("res2: " + str(res2))
