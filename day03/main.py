
def part_one(data):
  
  sum = 0
  
  for bank in data:
    digits = list(bank)
    
    d1 = digits.index(max(digits))
    
    if d1 == len(digits) - 1:
      d2 = digits.index(max(digits[:d1]))
      sum += int(digits[d2])*10 + int(digits[d1])
    else:
      d2 = digits.index(max(digits[d1+1:]))  
      sum += int(digits[d1])*10 + int(digits[d2])
  
  return sum


def part_two(data):
  
  sum = 0
  
  for bank in data:
    digits = list(bank)
    
    # this could be used also for the first part, by changing the length to 2
    # but nvm, it's late
    while len(digits) > 12:
      for i in range(1, len(digits)):
        if digits[i] > digits[i-1]: 
          del digits[i-1]
          break
      else:
        del digits[i]
    
    joltage = int(''.join(digits))
    sum += joltage
  
  return sum


def read_input(filename: str):
  with open(filename, 'r') as file:
    return [line.strip() for line in file.readlines()]
  

if __name__ == "__main__":
  input_data = read_input('input.txt')

  print("Part one:", part_one(input_data))
  print("Part two:", part_two(input_data))