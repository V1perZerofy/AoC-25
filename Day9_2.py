from collections import deque


def read_input(path):
    reds = []
    with open(path) as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            reds.append((x, y))
    return reds


def build_boundary(reds):
    boundary = set(reds)

    n = len(reds)
    for i in range(n):
        x1, y1 = reds[i]
        x2, y2 = reds[(i + 1) % n]

        if x1 == x2:  # vertical
            step = 1 if y2 > y1 else -1
            for y in range(y1, y2 + step, step):
                boundary.add((x1, y))
        else:  # horizontal
            step = 1 if x2 > x1 else -1
            for x in range(x1, x2 + step, step):
                boundary.add((x, y1))

    return boundary


def fill_interior(boundary):
    xs = [x for x, _ in boundary]
    ys = [y for _, y in boundary]

    minx, maxx = min(xs) - 1, max(xs) + 1
    miny, maxy = min(ys) - 1, max(ys) + 1

    outside = set()
    q = deque([(minx, miny)])

    while q:
        x, y = q.popleft()
        if (x, y) in outside:
            continue
        if (x, y) in boundary:
            continue
        if not (minx <= x <= maxx and miny <= y <= maxy):
            continue

        outside.add((x, y))
        q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

    inside = {
        (x, y)
        for x in range(minx + 1, maxx)
        for y in range(miny + 1, maxy)
        if (x, y) not in outside and (x, y) not in boundary
    }

    return boundary | inside, minx + 1, miny + 1, maxx - 1, maxy - 1


def build_prefix_sum(allowed, minx, miny, maxx, maxy):
    w = maxx - minx + 1
    h = maxy - miny + 1

    grid = [[0] * (h + 1) for _ in range(w + 1)]

    for x, y in allowed:
        grid[x - minx + 1][y - miny + 1] = 1

    psum = [[0] * (h + 1) for _ in range(w + 1)]
    for x in range(1, w + 1):
        for y in range(1, h + 1):
            psum[x][y] = (
                grid[x][y] + psum[x - 1][y] + psum[x][y - 1] - psum[x - 1][y - 1]
            )

    return psum, minx, miny


def rect_sum(psum, x1, y1, x2, y2):
    return psum[x2][y2] - psum[x1 - 1][y2] - psum[x2][y1 - 1] + psum[x1 - 1][y1 - 1]


def largest_rectangle_part_two(reds):
    red_set = set(reds)
    boundary = build_boundary(reds)

    allowed, minx, miny, maxx, maxy = fill_interior(boundary)
    psum, ox, oy = build_prefix_sum(allowed, minx, miny, maxx, maxy)

    red_pts = list(red_set)
    best = 0

    for i in range(len(red_pts)):
        x1, y1 = red_pts[i]
        for j in range(i + 1, len(red_pts)):
            x2, y2 = red_pts[j]

            if x1 == x2 or y1 == y2:
                continue

            xa, xb = sorted([x1, x2])
            ya, yb = sorted([y1, y2])

            area = (xb - xa + 1) * (yb - ya + 1)
            if area <= best:
                continue

            sx1 = xa - ox + 1
            sy1 = ya - oy + 1
            sx2 = xb - ox + 1
            sy2 = yb - oy + 1

            if rect_sum(psum, sx1, sy1, sx2, sy2) == area:
                best = area

    return best


if __name__ == "__main__":
    reds = read_input("inputs/input9.txt")
    print(largest_rectangle_part_two(reds))
