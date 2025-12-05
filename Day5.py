with open("inputs/input5.txt") as f:
    lines = f.read().strip().split("\n\n")
    ranges, ids = lines[0].split("\n"), lines[1].split("\n")

ranges = sorted([tuple(map(int, i.split("-"))) for i in ranges])

def inRange(value):
    for start, end in ranges:
        if int(start) <= int(value) <= int(end):
            return True
    return False

res = 0
for i in ids:
    if inRange(i):
        res += 1

res2 = 0
curr_start, curr_end = ranges[0]

for start, end in ranges[1:]:
    if start <= curr_end + 1:
        curr_end = max(end, curr_end)
    else:
        res2 += curr_end - curr_start + 1
        curr_start, curr_end = start, end

res2 += curr_end - curr_start + 1

print(res)
print(res2)
