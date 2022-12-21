def main():
    data = dict()
    with open('input.txt') as f:
        for line in f:
            name, operation = line.strip().split(': ')
            data[name] = int(operation) if operation.isdigit() else operation
    solve(data)


def solve(data):
    print(calc_mokeys('root', data))


def calc_mokeys(node, data):
    if isinstance(data[node], int):
        return data[node]
    val1, op, val2 = data[node].split()
    # print(f"{calc_mokeys(val1, data)} {op} {calc_mokeys(val2, data)}")
    return int(eval(f"{calc_mokeys(val1, data)} {op} {calc_mokeys(val2, data)}"))


if __name__ == '__main__':
    main()
