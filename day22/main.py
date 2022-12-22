import re


def main():
    with open('input.txt') as f:
        m, path = f.read().split('\n\n')
        m = m.split('\n')
        grid = []
        max_col = 0
        for line in m:
            max_col = max(max_col, len(line))
        for line in m:
            if len(line) < max_col:
                line += '_' * (max_col - len(line))
            grid.append(['_' if c == ' ' else c for c in line])
        path = [(int(x), d) for x, d in re.findall(r"(\d+)([A-Z])", path)]
    print(solve(grid, path))


def solve(grid, path):
    row, col = 0, grid[0].index('.')
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d_pointer = 0
    for steps, turn in path:
        for _ in range(steps):
            row, col = move(grid, directions[d_pointer], row, col)
        if turn == 'R':
            d_pointer = (d_pointer + 1) % 4
        elif turn == 'L':
            d_pointer = (d_pointer - 1) % 4
    final_col = col + 1
    final_row = row + 1
    return final_row * 1000 + final_col * 4 + d_pointer


# helper function
def plot_grid(grid):
    for row in grid:
        line = ""
        for c in row:
            line += " " if c == "_" else c
        print(line)


def move(grid, direction, row, col):
    dr, dc = direction
    nr, nc = row + dr, col + dc
    if dr == -1:  # up
        if nr < 0 or grid[nr][nc] == '_':
            nr = find_bottom_row(nc, grid)
    elif dr == 1:  # down
        if nr >= len(grid) or grid[nr][nc] == '_':
            nr = find_top_row(nc, grid)
    elif dc == -1:  # left
        if nc < 0 or grid[nr][nc] == '_':
            nc = find_right_col(nr, grid)
    elif dc == 1:  # right
        if nc >= len(grid[nr]) or grid[nr][nc] == '_':
            nc = find_left_col(nr, grid)

    if grid[nr][nc] == '#':
        return row, col
    return nr, nc


def find_top_row(nc, grid):
    for i, r in enumerate(grid):
        if r[nc] in '.#':
            return i


def find_bottom_row(nc, grid):
    for i, r in enumerate(grid[::-1]):
        if r[nc] in '.#':
            return len(grid) - i - 1


def find_left_col(nr, grid):
    for i, c in enumerate(grid[nr]):
        if c in '.#':
            return i


def find_right_col(nr, grid):
    for i, c in enumerate(grid[nr][::-1]):
        if c in '.#':
            return len(grid[nr]) - i - 1


if __name__ == '__main__':
    main()
