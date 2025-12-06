
def part_one(data):
  
  grand_total = 0
  
  operations_queue = data[-1].split()
  number_cols = [ [] for _ in range(len(operations_queue)) ]
  
  for row in data[:-1]:
    nums = row.split()
    for i in range(len(nums)):
      number_cols[i].append(nums[i])
  
  ops = {
    '+': lambda col: sum(int(x) for x in col),
    '*': lambda col: eval('*'.join(col))
  }

  for i in range(len(operations_queue)):
    # che flex applicare sta roba
    grand_total += ops[operations_queue[i]](number_cols[i])

  return grand_total

def part_two(data):
  from math import prod               # cheating a bit here
  from itertools import zip_longest

  # reading columns instead of rows (transposing the matrix)
  cols = list(zip_longest(*data, fillvalue=' '))
  
  number_groups = []
  current_group = []
  
  for col in cols:
    if any(c != ' ' for c in col):
      digit_part = ''.join(c for c in col[:-1] if c.isdigit())
      if digit_part:
        current_group.append(digit_part)
    else:
      if current_group:
        number_groups.append(current_group)
        current_group = []
  
  if current_group:
    number_groups.append(current_group)
  
  operations_queue = [col[-1] for col in cols if col[-1] in ['+', '*']]
  
  ops = {
    '+': lambda col: sum(int(x) for x in col),
    '*': lambda col: prod(int(x) for x in col)
  }

  grand_total = 0
  for i in range(len(operations_queue)):
    grand_total += ops[operations_queue[i]](number_groups[i])

  return grand_total


def read_input(filename: str):
  with open(filename, 'r') as file:
    return [line.strip() for line in file.readlines()]
  

if __name__ == "__main__":
  input_data = read_input('input.txt')

  print("Part one:", part_one(input_data))
  print("Part two:", part_two(input_data))