
def split_data(data):
  
  ranges = []
  ids = []
  
  empty_line_idx = data.index('')
  
  for line in data[:empty_line_idx]:
    parts = line.split('-')
    ranges.append((int(parts[0]), int(parts[1])))
  
  for line in data[empty_line_idx + 1:]:
    if line:
      ids.append(int(line))
      
  return ranges, ids


def part_one(data):

  ranges, ids = split_data(data)
  
  # consider overlapping ranges
  merged_ranges = []
  for start, end in sorted(ranges):
    if merged_ranges and start <= merged_ranges[-1][1] + 1:
      merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
    else:
      merged_ranges.append((start, end))
      
  fresh_ids = 0
  for id in ids:
    if any(start <= id <= end for start, end in merged_ranges):
      fresh_ids += 1

  return fresh_ids


def part_two(data):
  
  ranges, ids = split_data(data)
  
  merged_ranges = []
  for start, end in sorted(ranges):
    if merged_ranges and start <= merged_ranges[-1][1] + 1:
      merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
    else:
      merged_ranges.append((start, end))
    
  # we do not create a list of single fresh ids, my computer would explode.
  fresh_ids_count = sum(end - start + 1 for start, end in merged_ranges)
  
  return fresh_ids_count


def read_input(filename: str):
  with open(filename, 'r') as file:
    return [line.strip() for line in file.readlines()]
  

if __name__ == "__main__":
  input_data = read_input('input.txt')

  print("Part one:", part_one(input_data))
  print("Part two:", part_two(input_data))