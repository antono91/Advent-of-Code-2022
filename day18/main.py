from collections import deque


def main():
    with open('input.txt') as f:
        data = [tuple(map(int, line.strip().split(','))) for line in f]

    print(solve(data))


def solve(data):
    part1 = 0
    for x, y, z in data:
        part1 += len([n for n in get_neighbors(x, y, z) if n not in data])
    part2 = flood_fill(data)
    return part1, part2


def get_neighbors(x, y, z):
    neighbors = []
    for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        neighbors.append((x + dx, y + dy, z + dz))
    return neighbors


def flood_fill(data):
    _x = [x for (x, y, z) in data]
    _y = [y for (x, y, z) in data]
    _z = [z for (x, y, z) in data]

    min_coord, max_coord = min(_x + _y + _z) - 1, max(_x + _y + _z) + 1

    outside_faces = 0
    q = deque([(min_coord, min_coord, min_coord)])
    seen = set()
    while q:
        p = q.popleft()
        if p in seen:
            continue
        seen.add(p)
        for n in get_neighbors(*p):
            if n not in data and all(max_coord >= coord >= min_coord for coord in n):
                q.append(n)
            elif n in data:
                outside_faces += 1

    return outside_faces


if __name__ == '__main__':
    main()
