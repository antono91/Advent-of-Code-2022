from sympy import solve as s


def main():
    data = dict()
    with open('input.txt') as f:
        for line in f:
            name, operation = line.strip().split(': ')
            data[name] = operation
    print(solve(data))


def solve(data):
    part1 = int(eval(calc_mokeys('root', data, False)))

    # Part2
    data['humn'] = 'x'
    left, _, right = data['root'].split()

    left = calc_mokeys(left, data, True)
    right = calc_mokeys(right, data, True)
    humn_side = left if 'x' in left else right
    other_side = left if 'x' not in left else right

    part2 = int(s(f"{humn_side} - {other_side}")[0])

    return part1, part2


def calc_mokeys(node, data, part2):
    if data[node].isdigit():
        return data[node]
    if node == 'humn' and part2:
        return 'x'
    val1, op, val2 = data[node].split()
    return f"({calc_mokeys(val1, data, part2)} {op} {calc_mokeys(val2, data, part2)})"


if __name__ == '__main__':
    main()
