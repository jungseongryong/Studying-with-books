n = int(input())

x, y = 1, 1

steps = input().split()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
move = ['R', 'L', 'U', 'D']

for step in steps:
  for i in range(4):
    if step == move[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  x, y = nx, ny

print(x, y)
