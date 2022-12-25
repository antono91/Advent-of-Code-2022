import re


def main():
    print(solve(*parse_input('input.txt'), True))
    print(solve(*parse_input('input.txt'), False))


def parse_input(file):
    with open(file) as f:
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
    return grid, path


def solve(grid, path, part1):
    row, col = 0, grid[0].index('.')
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d_pointer = 0
    for steps, turn in path:
        for _ in range(steps):
            row, col = move(grid, directions[d_pointer], row, col, part1)
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


def move(grid, direction, row, col, part1):
    dr, dc = direction
    nr = (row + dr) % len(grid)
    nc = (col + dc) % len(grid[0])
    if part1:
        while grid[nr][nc] == '_':
            nr = (nr + dr) % len(grid)
            nc = (nc + dc) % len(grid[0])
    else:
        if len(grid[0]) <= nc < 0 or len(grid) <= nr < 0 or grid[nr][nc] == '_':
            find_next_face(row, col, dr, dc)

    if grid[nr][nc] == '#':
        return row, col
    return nr, nc


def find_next_face(row, col, dr, dc):
    face_transition = {
        1, (0, -1):
    }
    face = (row // 50) * 3 + col // 50



if __name__ == '__main__':
    main()

#       A B
#       C
#     D E
#     F
#    A > B(>)    B > E(<)    C > B(^)    D > E(>)    E > B(<)    F > E(^)
#    A < D(>)    B < A(<)    C < D(v)    D < A(>)    E < D(<)    F < A(v)
#    A v C(v)    B v C(<)    C v E(v)    D v F(v)    E v F(<)    F v B(v)
#    A ^ F(>)    B ^ F(^)    C ^ A(^)    D ^ C(>)    E ^ C(^)    F ^ D(^)
