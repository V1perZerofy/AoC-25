import numpy as np

with open("inputs/input9.txt") as f:
    lines = f.read().strip().split("\n")

all_distances = []
for l1 in range(len(lines)):
    for l2 in range(l1 + 1, len(lines)):
        acords = np.array(tuple(map(int, lines[l1].split(","))))
        bcords = np.array(tuple(map(int, lines[l2].split(","))))

        d = np.sum((acords - bcords) ** 2)

        all_distances.append(
            (
                tuple(map(int, lines[l1].split(","))),
                tuple(map(int, lines[l2].split(","))),
                float(d),
            )
        )


all_distances = sorted(all_distances, key=lambda all_distances: all_distances[2])

circuits = []
last = None
for i in all_distances:
    a, b, *_ = i
    i, j = None, None
    for idx, circuit in enumerate(circuits):
        if a in circuit:
            i = idx
        if b in circuit:
            j = idx

    if i is None and j is None:
        circuits.append({a, b})
    elif i is not None and j is None:
        circuits[i].add(b)
        if len(circuits) == 1 and len(circuits[0]) == len(lines):
            last = (a, b)
            print("Fully connected at", a, b)
            break
    elif i is None and j is not None:
        circuits[j].add(a)
        if len(circuits) == 1 and len(circuits[0]) == len(lines):
            last = (a, b)
            print("Fully connected at", a, b)
            break
    elif i == j:
        pass
    elif i is not None and j is not None:
        circuits[i] |= circuits[j]
        del circuits[j]
        if len(circuits) == 1 and len(circuits[0]) == len(lines):
            last = (a, b)
            print("Fully connected at", a, b)
            break

circuits = sorted(circuits, key=len)

res = 1

print(len(circuits))
print(len(circuits[0]))

if last:
    a, b = last
    x1, *m = a
    x2, *n = b

    print(x1, x2)
    print(x1 * x2)
