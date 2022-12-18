#!/usr/local/bin/python
from collections import deque


def main():
    with open('input.txt') as f:
        data = [tuple(map(int, line.strip().split(','))) for line in f] 

    print(solve1(data))
    print(solve2(data))


def solve1(data):
    faces = 0
    for x, y, z in data:
        if (x - 1, y, z) not in data:
            faces += 1
        if (x + 1, y, z) not in data:
            faces += 1
        if (x, y - 1, z) not in data:
            faces += 1
        if (x, y + 1, z) not in data:
            faces += 1
        if (x, y, z - 1) not in data:
            faces += 1
        if (x, y, z + 1) not in data:
            faces += 1
    return faces


outside = set()
inside = set()
def solve2(data):
    inside.clear()
    outside.clear()
    out_faces = 0

    for x, y, z in data:
        if flood_fill(x + 1, y, z, data):
            out_faces += 1
        if flood_fill(x - 1, y, z, data):
            out_faces += 1
        if flood_fill(x, y + 1, z, data):
            out_faces += 1
        if flood_fill(x, y - 1, z, data):
            out_faces += 1
        if flood_fill(x, y, z + 1, data):
            out_faces += 1
        if flood_fill(x, y, z - 1, data):
            out_faces += 1

    return out_faces


def flood_fill(x, y, z, data):
    if (x, y, z) in inside:
        return False
    if (x, y, z) in outside:
        return True

    q = deque([(x, y, z)])
    seen = set()
    while q:
        x, y, z = q.popleft()
        if (x, y, z) in data:
            continue
        if (x, y, z) in seen:
            continue
        seen.add((x, y, z))
        if len(seen) > 1500:
            for p in seen:
                outside.add(p)
            return True
        q.append((x+1, y, z))
        q.append((x-1, y, z))
        q.append((x, y-1, z))
        q.append((x, y+1, z))
        q.append((x, y, z-1))
        q.append((x, y, z+1))
    for p in seen:
        inside.add(p)
    return False


if __name__ == '__main__':
    main()
