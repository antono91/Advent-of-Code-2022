#!/usr/local/bin/python


def main():
    with open('input.txt') as f:
        data = [(i, int(line.strip())) for i, line in enumerate(f)]
    print(solve(data))


def solve(data):
    key = 811589153
    part1 = grove_coordinates(mixing(data.copy(), 1))
    part2 = grove_coordinates(mixing([(i, f * key) for i, f in data], 10))
    return part1, part2


def grove_coordinates(li):
    for i, item in enumerate(li):
        if item[1] == 0:
            return sum([li[(i + x) % len(li)][1] for x in [1000, 2000, 3000]])


def mixing(li, n):
    len_ = len(li)
    for _ in range(n):
        for ind in range(len_):
            for j, (i, v) in enumerate(li):
                if ind == i:
                    ind_to_move = j
                    break
            item = li.pop(ind_to_move)
            new_index = (ind_to_move + item[1]) % (len_ - 1)
            li = li[:new_index] + [item] + li[new_index:]
    return li


if __name__ == '__main__':
    main()
