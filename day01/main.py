
def part_one(data):
  
  point = 50
  zeros = 0
  
  for row in data:
    go_right = 1 if row[0] == "R" else 0
    amount = int(row[1:])
    
    point = (point + amount) % 100 if go_right else (point - amount) % 100
      
    if point == 0:
      zeros += 1
      
  return zeros


def part_two(data):
  """ enhanced version that also counts crossings of zero """
  
  point = 50
  zeros = 0
  
  for row in data:
    go_right = 1 if row[0] == "R" else -1
    amount = int(row[1:])
    
    # get each full cycle of 100
    zeros += amount // 100
    
    # remainder is next value pointing
    remainder = amount % 100
    
    if remainder > 0:
      new_point = point + go_right * remainder
      
      # check if we crossed zero
      if (go_right > 0 and new_point >= 100) or (go_right < 0 and new_point < 1 and point > 0):
        zeros += 1
      
      point = (new_point + 100) % 100
      
  return zeros



def read_input(filename: str):
  with open(filename, 'r') as file:
    return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
  input_data = read_input('input.txt')
  print("Part one:", part_one(input_data))
  print("Part two:", part_two(input_data))