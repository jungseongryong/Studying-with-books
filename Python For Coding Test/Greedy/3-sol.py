n, m = map(int, input().split())

result = 0
for i in range(n):
  row = list(map(int, input().split()))

  result = max(result, min(row))

print(result)
