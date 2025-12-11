from collections import defaultdict

def count_paths(graph, start, end, memo=None):
  # recursively counting all paths from start to end using memoization <3
  if memo is None:
    memo = {}
  if start == end:
    return 1
  if start in memo:
    return memo[start]

  # sum paths through all neighbors
  total = sum([count_paths(graph, neighbor, end, memo) for neighbor in graph[start]])
  memo[start] = total
  return total

def part_one(data):
  # build graph from input data
  G = defaultdict(list)
  for line in data:
    a, destinations = line.split(': ')
    for b in destinations.split(' '):
      G[a].append(b)
      
  # count paths from 'you' to 'out'
  return count_paths(G, 'you', 'out', None)

def part_two(data):
  # build graph from input data
  G = defaultdict(list)
  for line in data:
    a, destinations = line.split(': ')
    for b in destinations.split(' '):
      G[a].append(b)

  # calculate paths through three segments (assuming 'dac -> fft' is impossible)
  p2 = count_paths(G, 'svr', 'fft') * count_paths(G, 'fft', 'dac') * count_paths(G, 'dac', 'out')
  return p2

def read_input(filename: str):
  with open(filename, 'r') as file:
      return [line.strip() for line in file.readlines()]

if __name__ == '__main__':
    input_data = read_input('input.txt')
    print("Part one:", part_one(input_data))
    print("Part two:", part_two(input_data))
