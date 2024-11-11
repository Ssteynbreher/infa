import math
treasure_map = [
    [1, 2],
    [3, 5],
    [5, 6],
    [7, 8]
]
def f(treasure_map, alex_coords):
  cl_tr = treasure_map[0]
  md = math.sqrt((alex_coords[0] - cl_tr[0])**2 + (alex_coords[1] - cl_tr[1])**2)
  for tr in treasure_map:
    d = math.sqrt((alex_coords[0] - tr[0])**2 + (alex_coords[1] - tr[1])**2)
    if d < md:
      md = d
      cl_tr = tr
  return cl_tr
alex_x = int(input("Введите координату X Александра: "))
alex_y = int(input("Введите координату Y Александра: "))
cl_tr = f(treasure_map, [alex_x, alex_y])
print("Координаты ближайшего сокровища: ", *(cl_tr))
