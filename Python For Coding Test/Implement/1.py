N = int(input())

point = [1, 1]
shift = list(input().split())
for i in shift:

  if i == 'R':
    if point[1] == N:
      continue
    point[1] += 1

  elif i == 'L':
    if point[1] == 1:
      continue
    point[1] -= 1

  elif i == 'U':
    if point[0] == 1:
      continue
    point[0] -= 1

  else:
    if point[0] == N:
      continue
    point[0] += 1

print(point[0], point[1])
