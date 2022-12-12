import copy


def main():
    with open('input.txt') as f:
        data = f.read().split('\n\n')
        
    print(solve(copy.deepcopy(data), True))
    print(solve(data, False))


class Monkey:

    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test_val = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspect_count = 0

    def operate(self, item, p1):
        self.inspect_count += 1
        op, n = self.operation
        n = int(n) if n.isdigit() else item
        item = item * n if op == '*' else item + n
        return item // 3 if p1 else item

    def test(self, item):
        return item % self.test_val == 0


def solve(data, p1):
    monkeys = []
    for m in data:
        m = [x.strip() for x in m.split('\n')]
        items = [int(i) for i in m[1][16:].split(',')]
        operation = m[2][21:].split()
        test = int(m[3][19:])
        if_true = int(m[4][25:])
        if_false = int(m[5][26:])
        monkeys.append(Monkey(items, operation, test, if_true, if_false))

    max_div = 1
    for m in monkeys:
        max_div *= m.test_val

    for _ in range(20 if p1 else 10000):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.pop(0) % max_div
                item = monkey.operate(item, p1)
                other = monkey.if_true if monkey.test(
                    item) else monkey.if_false
                monkeys[other].items.append(item)

    x, y = sorted([monkey.inspect_count for monkey in monkeys])[-2:]
    return x * y


if __name__ == '__main__':
    main()
