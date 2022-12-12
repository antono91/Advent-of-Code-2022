def main():
  with open('input.txt', 'r') as f:
    data = [sum(map(int, block.split("\n"))) for block in f.read().split("\n\n")]
  print(solve(data))

  
def solve(data):
  return max(data), sum(sorted(data)[-3:])


if __name__ == '__main__':
  main()
