n, k = map(int, input().split())

result = 0
while True:
  target = (n // k) * k
  result += (n - target + 1)

  n = target // k
  if k > n:
    break

result += n - 1
print(result)
