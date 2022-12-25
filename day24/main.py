from collections import deque


def main():
    width = height = 0
    blizzards = list()
    walls = set()
    with open('input.txt') as f:
        lines = f.read().split()
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                if c == '#': walls.add((x, y))
                if c == ">": blizzards.append((x, y, 1, 0))
                if c == "<": blizzards.append((x, y, -1, 0))
                if c == "^": blizzards.append((x, y, 0, -1))
                if c == "v": blizzards.append((x, y, 0, 1))
                width = max(width, x)
                height = max(height, y)
    blizzards_by_t = create_blizzard_dict(blizzards, width, height)
    print(solve(blizzards_by_t, walls, width, height))


# helper function
def plot(blizzards, width, height):
    for r in range(height + 1):
        if r == 0 or r == height:
            print('#' * (width + 1))
            continue
        line = ""
        for c in range(width + 1):
            if c == 0 or c == width:
                line += "#"
            elif (c, r, 1, 0) in blizzards:
                line += '>'
            elif (c, r, -1, 0) in blizzards:
                line += '<'
            elif (c, r, 0, -1) in blizzards:
                line += '^'
            elif (c, r, 0, 1) in blizzards:
                line += 'v'
            else:
                line += '.'

        print(line)
    print()


def solve(blizzards_by_t, walls, width, height):
    seen = set()
    p1, part1 = False, 0
    reached_end = reached_start = False
    q = deque([(1, 0, 0, reached_end, reached_start)])
    while q:
        x, y, t, reached_end, reached_start = q.popleft()
        if x < 0 or x > width or y < 0 or y > height or (x, y) in walls:
            continue
        if y == height and reached_end and reached_start:
            return part1, t
        if y == height and not p1:
            p1 = True
            part1 = t
        if y == height:
            reached_end = True
        if reached_end and y == 0:
            reached_start = True

        if (x, y, t, reached_end, reached_start) in seen:
            continue
        seen.add((x, y, t, reached_end, reached_start))

        blizzards = blizzards_by_t[(t + 1) % len(blizzards_by_t)]

        if (x, y) not in blizzards:
            q.append((x, y, t + 1, reached_end, reached_start))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in blizzards:
                q.append((nx, ny, t + 1, reached_end, reached_start))


def create_blizzard_dict(blizzards, width, height):
    blizzards_by_t = {0: set((x, y) for x, y, _, _ in blizzards)}
    for t in range(1, (width - 1) * (height - 1) - 1):
        for _ in range(len(blizzards)):
            x, y, dx, dy = blizzards.pop(0)
            nx, ny = x + dx, y + dy
            ny = 1 if ny >= height else height - 1 if ny < 1 else ny
            nx = 1 if nx >= width else width - 1 if nx < 1 else nx
            blizzards.append((nx, ny, dx, dy))
        blizzards_by_t[t] = set((x, y) for x, y, _, _ in blizzards)
    return blizzards_by_t


if __name__ == '__main__':
    main()
