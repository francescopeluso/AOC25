# this is a pattern matching problem, yay!

import re

def part_one(data):
  
  invalid_ids_sum = 0
  
  for start, end in data:
    for id in range(start, end + 1):
      id_str = str(id)
      if len(id_str) % 2 == 0:
        half = len(id_str) // 2
        if id_str[:half] == id_str[half:]:
          invalid_ids_sum += id
  
  return invalid_ids_sum

def part_two(data):
  
  invalid_ids_sum = 0
  
  for start, end in data:
    for id in range(start, end + 1):
      id_str = str(id)
      length = len(id_str)
            
      for pattern_len in range(1, length // 2 + 1):
        
        # if the length of the id is divisible by the pattern length,
        # we can check if the pattern repeated forms the id.
        if length % pattern_len == 0:
          pattern = id_str[:pattern_len]
          repetitions = length // pattern_len
          
          # stupid example: 222222 is a invalid id. 222221 is not.
          # pattern must match the whole id, not just part of it.
          if pattern * repetitions == id_str:
            invalid_ids_sum += id   
            break     
      
  return invalid_ids_sum

def read_input(filename: str):
  with open(filename, 'r') as file:
    return [line.strip() for line in file.readlines()]
  
def get_ranges(data):
  results = []
  ranges = data[0].split(',')
  for range in ranges:
    start, end = range.split('-')
    results.append((int(start), int(end)))
  return results

if __name__ == "__main__":
  input_data = read_input('input.txt')
  ranges = get_ranges(input_data)  
  print("Part one:", part_one(ranges))
  print("Part two:", part_two(ranges))