from collections import deque


def main():
    with open('input.txt') as f:
        data = [[ord(x) - 96 if x.islower() else x for x in line.strip()] for line in f]

    for r, row in enumerate(data):
        for c, col in enumerate(data[r]):
            if col == 'S':
                start = (c, r)
                data[r][c] = 1
            if col == 'E':
                end = (c, r)
                data[r][c] = 26

    print(bfs(data, start, end, True))
    print(bfs(data, start, end, False))


def bfs(grid, start, end, part1):
    start = start if part1 else end

    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        cond1 = (part1 and (x, y) == end) or (not part1 and grid[y][x] == 1)
        if cond1:
            return len(path) - 1
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid):
                cond2 = (grid[y2][x2] - grid[y][x] <= 1 and part1) or (grid[y2][x2] - grid[y][x] >= -1 and not part1)
                if cond2 and (x2, y2) not in visited:
                    queue.append(path + [(x2, y2)])
                    visited.add((x2, y2))


if __name__ == '__main__':
    main()
