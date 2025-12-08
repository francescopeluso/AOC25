
# union-find data structure to group connected boxes
# never studied this in university, had to look it up lol
class UnionFind:
  
  def __init__(self, items):
    # each item starts as its own parent
    self.parent = {}
    self.rank = {}
    for item in items:
      self.parent[item] = item
      self.rank[item] = 0
  
  # find the root of an item with path compression
  def find(self, item):
    if self.parent[item] != item:
      self.parent[item] = self.find(self.parent[item])
    return self.parent[item]
  
  # merge two sets together
  def union(self, item1, item2):
    root1 = self.find(item1)
    root2 = self.find(item2)
    
    # already in same set
    if root1 == root2:
      return
    
    # union by rank to keep tree balanced
    if self.rank[root1] < self.rank[root2]:
      self.parent[root1] = root2
    elif self.rank[root1] > self.rank[root2]:
      self.parent[root2] = root1
    else:
      self.parent[root2] = root1
      self.rank[root1] += 1


# calculate squared distance between two 3d points
def distance_squared(p1, p2):
  dx = p1[0] - p2[0]
  dy = p1[1] - p2[1]
  dz = p1[2] - p2[2]
  return dx*dx + dy*dy + dz*dz


def part_one(data):
  # parse input into list of 3d coordinates
  boxes = []
  for line in data:
    if line:
      x, y, z = map(int, line.split(','))
      boxes.append((x, y, z))
  
  # generate all possible pairs of boxes
  pairs = []
  for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
      pairs.append((boxes[i], boxes[j]))
  
  # sort pairs by distance (closest first)
  pairs.sort(key=lambda p: distance_squared(p[0], p[1]))
  
  # connect the 1000 closest pairs
  uf = UnionFind(boxes)
  for box1, box2 in pairs[:1000]:
    uf.union(box1, box2)
  
  # group boxes into their circuits
  circuits = {}
  for box in boxes:
    circuit_id = uf.find(box)
    if circuit_id not in circuits:
      circuits[circuit_id] = []
    circuits[circuit_id].append(box)
  
  # multiply the sizes of the three largest circuits
  circuit_sizes = []
  for circuit in circuits.values():
    circuit_sizes.append(len(circuit))
  circuit_sizes.sort()
  
  result = circuit_sizes[-1] * circuit_sizes[-2] * circuit_sizes[-3]
  return result


def part_two(data):
  # parse input into list of 3d coordinates
  boxes = []
  for line in data:
    if line:
      x, y, z = map(int, line.split(','))
      boxes.append((x, y, z))
  
  # generate all possible pairs of boxes
  pairs = []
  for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
      pairs.append((boxes[i], boxes[j]))
  
  # sort pairs by distance (closest first)
  pairs.sort(key=lambda p: distance_squared(p[0], p[1]))
  
  # from now on, the difference is that we keep connecting boxes
  # until all boxes are in one circuit
  
  uf = UnionFind(boxes)
  
  # keep connecting boxes until everything is in one circuit
  for box1, box2 in pairs:
    uf.union(box1, box2)
    
    # count how many separate circuits we have
    circuit_ids = set()
    for box in boxes:
      circuit_ids.add(uf.find(box))
    
    # if all boxes are connected, return the result
    if len(circuit_ids) == 1:
      return box1[0] * box2[0]
  
  return -1



def read_input(filename: str):
  with open(filename, 'r') as file:
    return [line.strip() for line in file.readlines()]
  
  
if __name__ == "__main__":
  input_data = read_input('input.txt')

  print("Part one:", part_one(input_data))
  print("Part two:", part_two(input_data))