import re


def main():
    with open('input.txt') as f:
        data = [[(int(x[0]), int(x[1])) for x in re.findall('(\d+),(\d+)', line)]
                for line in f]

    print(solve(data, True))
    print(solve(data, False))


def plot_map(grid, max_y):
    x_ = [x[0] for x in grid]
    max_x, min_x = max(x_), min(x_)
    for y in range(0, max_y + 4):
        l = ''
        for x in range(min_x - 1, max_x + 1):
            l += grid[(x, y)] if (x, y) in grid else ' '
        print(l)


def simulate(grid, max_y, part1):
    down, left, right = (0, 1), (-1, 1), (1, 1)
    sx, sy = 500, 0
    rest = False
    while not rest:
        if part1:
            if sy > max_y:
                return grid, True
        else:
            if grid[(500, 0)] == 'o':
                return grid, True
        if not part1 and sy >= max_y:
            rest = True
        if (sx + down[0], sy + down[1]) not in grid:
            sy += 1
        elif (sx + left[0], sy + left[1]) not in grid:
            sx -= 1
            sy += 1
        elif (sx + right[0], sy + right[1]) not in grid:
            sx += 1
            sy += 1
        else:
            rest = True
    grid[(sx, sy)] = "o"
    return grid, False


def draw_paths(data):
    grid = dict()
    for line in data:
        for ((x1, y1), (x2, y2)) in zip(line, line[1::]):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    grid[(x1, y)] = "#"
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[(x, y1)] = "#"
    grid[(500, 0)] = "+"
    return grid


def solve(data, part1):
    grid = draw_paths(data)
    max_y = max([y[1] for y in grid])

    end = False
    while not end:
        grid, end = simulate(grid, max_y, part1)
    # plot_map(grid, max_y)
    return len([x for x in grid.values() if x == 'o'])


if __name__ == '__main__':
    main()
