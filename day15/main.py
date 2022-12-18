import re


def main():
    with open('input.txt') as f:
        data = [tuple(map(int, re.findall(r'-?\d+', line))) for line in f]
    print(solve(data))


def plot_map(m):
    H, W = 21, 26
    for r in range(-2, H):
        line = f"{r}\t"
        for c in range(-4, W):
            line += '#' if (c, r) in m else '.'
        print(line)


def get_ranges(data, row):
    ranges = []
    for sx, sy, bx, by in data:
        len_ = abs(sx - bx) + abs(sy - by)
        if sy - len_ <= row <= sy + len_:
            width = len_ - abs(row - sy)
            ranges.append((sx - width, sx + width))
    return reduce_ranges(ranges)


def reduce_ranges(ranges):
    ranges = sorted(ranges)
    res = []
    start, end = ranges[0]
    for s, e in ranges[1:]:
        if s <= end + 1:
            end = max(end, e)
        else:
            res.append((start, end))
            start = s
            end = e
    res.append((start, end))
    return res


def solve(data):
    start, end = get_ranges(data, 2_000_000)[0]
    part1 = end - start

    part2 = 0
    for i in range(4_000_001):
        ranges = get_ranges(data, i)
        if len(ranges) > 1:
            part2 = (ranges[0][-1] + 1) * 4_000_000 + i
            break
    return part1, part2


if __name__ == '__main__':
    main()
