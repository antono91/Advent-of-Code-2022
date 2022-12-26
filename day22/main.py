#!/usr/local/bin/python


import re


def main():
    m, path = parse_input('input.txt')
    print(solve(m, path, True))
    print(solve(m, path, False))


def parse_input(file):
    with open(file) as f:
        m, path = f.read().split('\n\n')
        m = m.split('\n')
        grid = []
        for line in m:
            if len(line) < 150:
                line += ' ' * (150 - len(line))
            grid.append([c for c in line])
        path = re.findall(r"\d+|L|R", path)
    return grid, path


def solve(grid, path, part1):
    path_list = list()
    row, col = 0, grid[0].index('.')
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d_pointer = 0

    for op in path:
        if op.isdigit():
            for s in range(int(op)):
                row, col, d_pointer = move(grid, directions[d_pointer], row, col, part1)
        else:
            if op == 'R':
                d_pointer = (d_pointer + 1) % 4
            elif op == 'L':
                d_pointer = (d_pointer - 1) % 4
    # plot_grid(grid, path_list)
    return (row + 1) * 1000 + (col + 1) * 4 + d_pointer


# helper function
def plot_grid(grid, path_list):
    for y, x, ch in path_list:
        grid[y][x] = ch
        for j, row in enumerate(grid):
            line = ""
            for i, c in enumerate(row):
                line += c
            print(line)


def move(grid, direction, row, col, part1):
    dr, dc = direction

    if part1:
        nr = (row + dr) % len(grid)
        nc = (col + dc) % len(grid[0])
        while grid[nr][nc] == ' ':
            nr = (nr + dr) % len(grid)
            nc = (nc + dc) % len(grid[0])
    else:
        nr, nc = row + dr, col + dc
        if len(grid[0]) <= nc or nc < 0 or len(grid) <= nr or nr < 0 or grid[nr][nc] == ' ':
            nr, nc, dr, dc = find_next_face(row, col, dr, dc)

    d_pointer = [(0, 1), (1, 0), (0, -1), (-1, 0)].index((dr, dc))

    if grid[nr][nc] == '#':
        return row, col, d_pointer
    return nr, nc, d_pointer


def find_next_face(row, col, dr, dc):
    face_transition = {
        (1, 0, -1): (0, 1, lambda r, c: (149 - r, 0)),
        (1, -1, 0): (0, 1, lambda r, c: (c - 50 + 150, 0)),
        (2, 0, 1): (0, -1, lambda r, c: (149 - r, 99)),
        (2, -1, 0): (-1, 0, lambda r, c: (199, c - 100)),
        (2, 1, 0): (0, -1, lambda r, c: (c - 100 + 50, 99)),
        (4, 0, 1): (-1, 0, lambda r, c: (49, r - 50 + 100)),
        (4, 0, -1): (1, 0, lambda r, c: (100, r - 50)),
        (6, 0, -1): (0, 1, lambda r, c: (49 - (r - 100), 50)),
        (6, -1, 0): (0, 1, lambda r, c: (c + 50, 50)),
        (7, 0, 1): (0, -1, lambda r, c: (49 - (r - 100), 149)),
        (7, 1, 0): (0, -1, lambda r, c: (150 + (c - 50), 49)),
        (9, 0, 1): (-1, 0, lambda r, c: (149, (r - 150) + 50)),
        (9, 0, -1): (1, 0, lambda r, c: (0, r - 150 + 50)),
        (9, 1, 0): (1, 0, lambda r, c: (0, c + 100))
    }
    face = row // 50 * 3 + col // 50
    dr, dc, f = face_transition[(face, dr, dc)]
    nr, nc = f(row, col)
    return nr, nc, dr, dc


if __name__ == '__main__':
    main()

    #       1 2
    #       4
    #     6 7
    #     9
    #    1 > 2(>)    2 > 7(<)    4 > 2(^)    6 > 7(>)    7 > 2(<)    9 > 7(^)
    #    1 < 6(>)    2 < 1(<)    4 < 6(v)    6 < 1(>)    7 < 6(<)    9 < 1(v)
    #    1 v 4(v)    2 v 4(<)    4 v 7(v)    6 v 9(v)    7 v 9(<)    9 v 2(v)
    #    1 ^ 9(>)    2 ^ 9(^)    4 ^ 1(^)    6 ^ 4(>)    7 ^ 4(^)    9 ^ 6(^)
