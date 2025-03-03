N, M = map(int, input().split())

s = set()

for i in range(M):
    v1, v2 = map(int, input().split())
    if v1 == v2:
        continue
    if v1 > v2:
        v1, v2 = v2, v1
    s.add((v1, v2))

print(M - len(s))