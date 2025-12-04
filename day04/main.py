
# forklift can only access a roll of paper '@' if there
# are FEWER THAN FOUR ROLLS IN THE 8 ADJACENT POSITIONS

# so we check for the top 3 rows, 3 cols and the ones
# on left and right. obv we skip the center cell as it
# is the roll we are checking

def count_adjacent_rolls(data, row, col):
  count = 0
  
  for row_offset in [-1, 0, 1]:
    for col_offset in [-1, 0, 1]:
      
      # skip the cell itself
      if row_offset == 0 and col_offset == 0:
        continue
      
      # neighbor coordinates
      nrow = row + row_offset
      ncol = col + col_offset
      
      # check if cell is within bounds and it is not wrapping around
      is_valid_row = 0 <= nrow < len(data)
      is_valid_col = 0 <= ncol < len(data[0])
      
      if is_valid_row and is_valid_col:
        if data[nrow][ncol] == '@':
          count += 1
  
  return count


def part_one(data):
  accessible = 0
  
  for row in range(len(data)):
    for col in range(len(data[0])):
      if data[row][col] == '@':
        if count_adjacent_rolls(data, row, col) < 4:
          accessible += 1
          
  return accessible


def part_two(data):
  grid = [list(row) for row in data]
  total_removed = 0
  
  while True:
    to_remove = []
    
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == '@':
          if count_adjacent_rolls(grid, row, col) < 4:
            to_remove.append((row, col))
    
    # if no rolls were removed, then we are done, else we continue
    if not to_remove:
      break
    
    # remove accessed rolls
    for row, col in to_remove:
      grid[row][col] = '.'
    
    total_removed += len(to_remove)
  
  return total_removed


def read_input(filename: str):
  with open(filename, 'r') as file:
    return [line.strip() for line in file.readlines()]
  

if __name__ == "__main__":
  input_data = read_input('input.txt')

  print("Part one:", part_one(input_data))
  print("Part two:", part_two(input_data))