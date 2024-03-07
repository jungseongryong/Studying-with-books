N, M = map(int, input().split())

matrix = []
for i in range(N):
  row = list(map(int, input().split()))
  matrix.append(row)

max = min(matrix[0])
for i in range(1,N):
  if max < min(matrix[i]):
    max = min(matrix[i])

print(max)