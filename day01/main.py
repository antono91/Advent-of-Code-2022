with open('input.txt', 'r') as f:
  data = [sum(map(int, block.split("\n"))) for block in f.read().split("\n\n")]


def solve(data):
  return max(data), sum(sorted(data)[-3:])


print(solve(data))