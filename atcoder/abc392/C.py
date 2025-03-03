N = int(input())

aA = [0] + list(map(int, input().split()))
aB = [0] + list(map(int, input().split()))

Res = [0] * (N + 1)
for i in range(1, N + 1):
    Res[aB[i]] = aB[aA[i]]

print(' '.join(map(str, Res[1:])))
