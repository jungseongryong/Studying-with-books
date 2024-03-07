N = int(input())

count = 0
for i in range(N + 1):
  if i == 3 or i == 13 or i == 23:
    count += 3600
  else:
    count += 1575

print(count)
