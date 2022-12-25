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


def solve(blizzards, walls, width, height):
    q = deque([(1, 0, 0)])
    seen = set()
    while q:
        x, y, t = q.popleft()
        if x < 0 or x > width or y < 0 or y > height or (x, y) in walls:
            continue
        if y == height:
            print(f"{x, y}Found end in: {t} minutes")
            break
        if (x, y, t) in seen:
            continue
        seen.add((x, y, t))

        blizzards = simulate_next_min(blizzards, width, height)
        blizzards_pos = {(x, y) for x, y, _, _ in blizzards}

        if (x, y) not in blizzards_pos:
            q.append((x, y, t + 1))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in blizzards_pos:
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
