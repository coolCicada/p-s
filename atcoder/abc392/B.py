N, M = map(int, input().split())

A_set = set(map(int, input().split()))

L = len(A_set)

TT = N - L
print(TT)

arr = []
for i in range(1, N + 1):
    if i not in A_set:
        arr.append(i)

if TT != 0:
    print(*arr)