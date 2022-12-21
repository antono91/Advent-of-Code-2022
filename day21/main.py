def main():
    data = dict()
    with open('input.txt') as f:
        for line in f:
            name, operation = line.strip().split(': ')
            data[name] = int(operation) if operation.isdigit() else operation
    solve(data)


def solve(data):
    # print(calc_mokeys('root', data))
    num1, _, num2 = data['root'].split()
    print(find_path(num1, data))


def calc_mokeys(node, data):
    if isinstance(data[node], int):
        return data[node]
    val1, op, val2 = data[node].split()

    # print(f"{calc_mokeys(val1, data)} {op} {calc_mokeys(val2, data)}")
    return int(eval(f"{calc_mokeys(val1, data)} {op} {calc_mokeys(val2, data)}"))


def find_path(node, data):
    if isinstance(data[node], int):
        # print(data[node], end="")
        return str(data[node])

    val1, op, val2 = data[node].split()
    print(node + "\n\t" + find_path(val1, data) + op + find_path(val2, data))
    return find_path(val1, data) + op + find_path(val2, data)



if __name__ == '__main__':
    main()
