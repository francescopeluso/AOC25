
def eval_rect_area(pair1, pair2):
  x1, y1 = pair1
  x2, y2 = pair2
  
  width = abs(x2 - x1) + 1
  height = abs(y2 - y1) + 1
  
  return width * height

def isPointInPolyOptimized(x, y, poly, poly_edges):
  """ checks if point is inside polygon using ray-casting. """
  
  n = len(poly)

  for (ux, uy), (vx, vy) in poly_edges:
    ux2 = ux * 2
    uy2 = uy * 2
    vx2 = vx * 2
    vy2 = vy * 2

    if ux == vx and ux2 == x:
      if uy2 <= vy2:
        if uy2 <= y <= vy2:
          return True
      elif vy2 <= y <= uy2:
        return True
    elif uy == vy and uy2 == y:
      if ux2 <= vx2:
        if ux2 <= x <= vx2:
          return True
      elif vx2 <= x <= ux2:
        return True

  intersections = 0
  j = n - 1
  for i in range(n):
    ux, uy = poly[i]
    vx, vy = poly[j]

    if ux == vx:
      uy2 = uy * 2
      vy2 = vy * 2
      ex = ux * 2

      if uy2 <= vy2:
        min_y, max_y = uy2, vy2
      else:
        min_y, max_y = vy2, uy2

      if min_y <= y < max_y and ex > x:
        intersections += 1

    j = i

  return (intersections & 1) == 1

def isValidRectangleOptimized(x1, x2, y1, y2, poly, poly_edges, pip_cache):
  """ checks if rectangle defined by (x1, y1) and (x2, y2) is valid within polygon. """
  
  mx = x1 + x2
  my = y1 + y2
  cache_key = (mx, my)

  if cache_key in pip_cache:
    if not pip_cache[cache_key]:
      return False
  else:
    in_poly = isPointInPolyOptimized(mx, my, poly, poly_edges)
    
    # using cache to avoid redundant calculations
    pip_cache[cache_key] = in_poly
    if not in_poly:
      return False

  for (ux, uy), (vx, vy) in poly_edges:
    if ux == vx:
      ex = ux
      if ex <= x1 or ex >= x2:
        continue

      if uy < vy:
        ey_min, ey_max = uy, vy
      else:
        ey_min, ey_max = vy, uy

      overlap_y_min = y1 if y1 > ey_min else ey_min
      overlap_y_max = y2 if y2 < ey_max else ey_max
      if overlap_y_min < overlap_y_max:
        return False

    else:
      ey = uy
      if ey <= y1 or ey >= y2:
        continue

      if ux < vx:
        ex_min, ex_max = ux, vx
      else:
        ex_min, ex_max = vx, ux

      overlap_x_min = x1 if x1 > ex_min else ex_min
      overlap_x_max = x2 if x2 < ex_max else ex_max
      if overlap_x_min < overlap_x_max:
        return False

  return True

###

def part_one(data):
  """ finding the largest rectangle that can be formed by any two points """
  
  xs, ys = zip(*(tuple(map(int, line.split(','))) for line in data))
  pairs = set(zip(xs, ys))
  
  pair_combos = [(p1, p2) for p1 in pairs for p2 in pairs if p1 != p2]
  
  max_area = 0
  
  for p1, p2 in pair_combos:
    area = eval_rect_area(p1, p2)
    if area > max_area:
      #print(f"New max area {area} from points {p1} and {p2}")
      max_area = area
  
  return max_area


def part_two(data):
  """ finding the largest rectangle using only red and green tiles """
  from typing import List, Tuple
  
  # parsing the red tile coordinates
  xs, ys = zip(*(tuple(map(int, line.split(','))) for line in data))
  coords = list(zip(xs, ys))
  
  if not coords:
    return 0

  n = len(coords)
  max_area = 0

  # build polygon edges
  poly_edges = []
  for i in range(n):
    u = coords[i]
    v = coords[(i + 1) % n]
    poly_edges.append((u, v))

  xs = [p[0] for p in coords]
  ys = [p[1] for p in coords]
  min_x, max_x = min(xs), max(xs)
  min_y, max_y = min(ys), max(ys)

  pip_cache = {}

  # check all pairs of coordinates for valid rectangles
  for i in range(n):
    x1, y1 = coords[i]

    for j in range(i + 1, n):
      x2, y2 = coords[j]

      if x1 < x2:
        rx1, rx2 = x1, x2
      else:
        rx1, rx2 = x2, x1

      if y1 < y2:
        ry1, ry2 = y1, y2
      else:
        ry1, ry2 = y2, y1

      width = rx2 - rx1 + 1
      height = ry2 - ry1 + 1
      area = width * height

      if area <= max_area:
        continue

      if rx1 < min_x or rx2 > max_x or ry1 < min_y or ry2 > max_y:
        continue

      if isValidRectangleOptimized(
        rx1, rx2, ry1, ry2, coords, poly_edges, pip_cache
      ):
        max_area = area

  return max_area


###

def read_input(filename: str):
  with open(filename, 'r') as file:
    return [line.strip() for line in file.readlines()]
  

if __name__ == "__main__":
  input_data = read_input('input.txt')

  print("Part one:", part_one(input_data))
  print("Part two:", part_two(input_data))