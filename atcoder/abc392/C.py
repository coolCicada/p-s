N = int(input())

aA = list(map(int, input().split()))
aB = list(map(int, input().split()))

dic = {}
for i in range(N):
    dic[aB[i]] = i

r = []
for i in range(N):
    r.append(aB[aA[dic[i + 1]] - 1])

print(' '.join(map(str, r)))