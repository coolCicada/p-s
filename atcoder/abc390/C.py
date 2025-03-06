H, W = map(int, input().split())

L = [input() for i in range(H)]

INF = float('inf')

l, r, t, b = INF, 0, INF, 0

for i in range(H):
    for j in range(W):
        if L[i][j] == '#':
            l = min(l, j)
            r = max(r, j)
            t = min(t, i)
            b = max(b, i)          

if l is INF:
    print('Yes')
    exit(0)

flag = True

for i in range(t, b + 1):
    for j in range(l, r + 1):
        if L[i][j] == '.':
            print('No')
            exit(0)

if flag:
    print('Yes')

