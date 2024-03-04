N, M, K = map(int, input().split())
# N: 배열의 크기
# M: 숫자가 더해지는 횟수
# K: 더할 때의 한계

nums = list(map(int, input().split()))
nums.sort()

max = nums[-1]
max2 = nums[-2]

sum = 0
k = 0
for _ in range(M):
  k += 1

  if k > K:
    sum += max2
    k = 0
  else:
    sum += max

print(sum)
