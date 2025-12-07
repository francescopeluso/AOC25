def visit(xy, grid, paths):
  """ Recursively visit the grid from position xy, counting splits and paths """
  
  x, y = xy
  
  # if out of bounds or already visited
  if xy in paths:
    return 0
  
  # if reached bottom
  if y == len(grid):
    paths[xy] = 1
    return 0
  
  # if we hit a splitter
  if grid[y][x] == '^':
    left = x - 1, y + 1
    right = x + 1, y + 1
    
    # count splits
    splits = 1 + visit(left, grid, paths) + visit(right, grid, paths)
    paths[xy] = paths[left] + paths[right]
    return splits
  
  splits = visit((x, y + 1), grid, paths)
  paths[xy] = paths[(x, y + 1)]
  
  return splits


def part_one(data):
  """ We need to count the number of splits from start to bottom """
  grid = data
  start = grid[0].index('S'), 0
  paths = {}
  return visit(start, grid, paths)

def part_two(data):
  """ We need to count the number of paths from start to bottom """
  grid = data
  start = grid[0].index('S'), 0
  paths = {}
  visit(start, grid, paths)
  return paths[start]


def read_input(filename: str):
  with open(filename, 'r') as file:
    return [line.strip() for line in file.readlines()]
  

if __name__ == "__main__":
  input_data = read_input('input.txt')

  print("Part one:", part_one(input_data))
  print("Part two:", part_two(input_data))