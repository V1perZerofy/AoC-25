with open("inputs/input9.txt") as f:
    lines = f.read().strip().split("\n")

res = 0
for line in range(len(lines)):
    for line2 in range(line + 1, len(lines)):
        ax, ay = lines[line].split(",")
        bx, by = lines[line2].split(",")

        dx = abs(int(bx) - int(ax)) + 1
        dy = abs(int(by) - int(ay)) + 1

        area = dx * dy

        if area > res:
            res = area

print(res)
