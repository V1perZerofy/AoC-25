from collections import defaultdict

with open("inputs/input9.txt") as f:
    lines = f.read().strip().split("\n")

lines = [(int(x), int(y)) for x, y in (line.split(",") for line in lines)]

# Part 1
res = 0
rects = []
for line in range(len(lines)):
    for line2 in range(line + 1, len(lines)):
        ax, ay = lines[line]
        dx, dy = lines[line2]
        bx, by = ax, dy
        cx, cy = dx, ay

        rects.append(((ax, ay), (bx, by), (cx, cy), (dx, dy)))

        lx = abs(int(dx) - int(ax)) + 1
        ly = abs(int(dy) - int(ay)) + 1

        area = lx * ly

        if area > res:
            res = area

print(res)


# Part 2
edges = []

n = len(lines)
for i in range(n):
    x1, y1 = lines[i]
    x2, y2 = lines[(i + 1) % n]

    assert x1 == x2 or y1 == y2

    edges.append(((x1, y1), (x2, y2)))


def pointOnSegment(xp, yp, x1, y1, x2, y2):
    dx1, dy1 = xp - x1, yp - y1
    dx2, dy2 = x2 - x1, y2 - y1
    if dx1 * dy2 != dy1 * dx2:
        return False

    return min(x1, x2) <= xp <= max(x1, x2) and min(y1, y2) <= yp <= max(y1, y2)


def isInside(edges, xp, yp):
    cnt = 0

    for (x1, y1), (x2, y2) in edges:
        if pointOnSegment(xp, yp, x1, y1, x2, y2):
            return True

        if y1 == y2:
            continue

        if not (y1 <= yp < y2):
            continue

        x_intersect = x1 + (yp - y1) * (x2 - x1) / (y2 - y1)

        if x_intersect >= xp:
            cnt += 1

    return cnt % 2 == 1


def intersectStrictAxisAligned(a, b, c, d):
    (x1, y1), (x2, y2) = a, b
    (x3, y3), (x4, y4) = c, d

    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    if x3 > x4:
        x3, x4 = x4, x3
    if y3 > y4:
        y3, y4 = y4, y3

    is_h1 = y1 == y2
    is_v1 = x1 == x2
    is_h2 = y3 == y4
    is_v2 = x3 == x4

    if is_h1 and is_h2:
        return False
    if is_v1 and is_v2:
        return False

    if is_v1:
        x1, y1, x2, y2, x3, y3, x4, y4 = x3, y3, x4, y4, x1, y1, x2, y2

    return x3 > x1 and x3 < x2 and y1 > y3 and y1 < y4


def rectEdges(rect):
    (ax, ay), (bx, by), (cx, cy), (dx, dy) = rect

    A = (int(ax), int(ay))
    B = (int(bx), int(by))
    C = (int(cx), int(cy))
    D = (int(dx), int(dy))

    corners = [A, C, D, B]

    edges = []
    for i in range(4):
        edges.append((corners[i], corners[(i + 1) % 4]))

    return edges


# debug
def print_polygon(points):
    # collect all boundary tiles (red + green)
    border = set(points)

    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]

        if x1 == x2:
            step = 1 if y2 > y1 else -1
            for y in range(y1 + step, y2, step):
                border.add((x1, y))
        else:
            step = 1 if x2 > x1 else -1
            for x in range(x1 + step, x2, step):
                border.add((x, y1))

    xs = [x for x, _ in border]
    ys = [y for _, y in border]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    red = set(points)

    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            if (x, y) in red:
                row.append("#")
            elif (x, y) in border:
                row.append("X")
            else:
                row.append(".")
        print("".join(row))


res2 = 0
for rect in rects:
    rect_edges = rectEdges(rect)
    valid = True

    for rect_edge in rect_edges:
        (x1, y1), (x2, y2) = rect_edge
        for (x3, y3), (x4, y4) in edges:
            if intersectStrictAxisAligned((x1, y1), (x2, y2), (x3, y3), (x4, y4)):
                valid = False
                break
        if not valid:
            break

    if not valid:
        continue

    (ax, ay), (_, _), (_, _), (dx, dy) = rect

    cx = (ax + dx) / 2
    cy = (ay + dy) / 2

    if not isInside(edges, cx, cy):
        continue

    lx = abs(dx - ax) + 1
    ly = abs(dy - ay) + 1
    area = lx * ly

    if area > res2:
        res2 = area


print_polygon(lines)
print(res2)
print(edges)
