N, D = map(int, input().split())

L = [0] * N

for i in range(N):
    L[i] = list(map(int, input().split()))


for i in range(1, D + 1):
    NA = list(map(lambda x: x[0] * (x[1] + i), L))
    NA.sort()
    print(NA[len(NA) - 1])