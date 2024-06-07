if __name__ == "__main__":
  num = int(input())
  coords = input()
  lst_coords = coords.split()
  lst_coords = [ int(x) for x in lst_coords ]
 
  lst_min = []
  for coord in range(min(lst_coords), max(lst_coords) + 1):
    new_ele = 0
    for _ in lst_coords:
      new_ele += (_-coord)**2
    lst_min.append(new_ele)
  minimum = min(lst_min)
  print(minimum)
