with open("inputs/input2.txt") as f:
    lines = f.read().strip().split(",")


invalid = []
invalid2 = []

for i in lines:
    x, y = i.split("-")
    for j in range(int(x), int(y)+1):
        jl = int(len(str(j)) / 2)
        if len(str(j)) % 2 == 0:
            if str(j)[0] == "0":
                break
            if str(j)[:jl] == str(j)[jl:]:
                invalid.append(int(j))




for i in lines:
    x, y = i.split("-")
    for j in range(int(x), int(y) + 1):
        for k in range(1, len(str(j))):
            if len(str(j)) % k == 0 and str(j)[:k] * (len(str(j)) // k) == str(j):
                if str(j)[0] == "0":
                    break
                invalid2.append(j)
                break

print(sum(invalid))
print(sum(invalid2))





