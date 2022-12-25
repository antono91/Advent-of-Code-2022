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

    solve(blizzards, walls, width, height)


def plot(blizzards, width, height):
    for r in range(height + 1):
        if r == 0 or r == height:
            print('#' * width)
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


def solve(blizzards, walls, width, height):
    sx, sy = 1, 0
    ex, ey = 5, 6
    q = deque([(sx, sy, 0)])
    seen = set()
    while q:
        blizzards_pos = {(x, y) for x, y, _, _ in blizzards}
        x, y, t = q.popleft()
        if width <= x <= 0 or height <= y <= 0 or (x, y) in walls:
            continue
        if y == ey:
            print(f"Found end in: {t} minutes")
            break
        if (x, y, t) in seen:
            continue
        seen.add((x, y, t))
        print(x, y, t)

        blizzards = simulate_next_min(blizzards, width, height)

        if (x, y) not in blizzards_pos:
            q.append((x, y, t))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if width <= nx < 0 or height <= ny < 0 or (nx, ny) in walls or (nx, ny) in blizzards_pos:
                continue

            q.append((nx, ny, t + 1))


def simulate_next_min(blizzards, width, height):
    for _ in range(len(blizzards)):
        x, y, dx, dy = blizzards.pop(0)
        nx, ny = x + dx, y + dy
        ny = 1 if ny >= height else height - 1 if ny < 1 else ny
        nx = 1 if nx >= width else width - 1 if nx < 1 else nx
        blizzards.append((nx, ny, dx, dy))
    return blizzards


if __name__ == '__main__':
    main()
