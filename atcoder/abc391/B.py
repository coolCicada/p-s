S, T = map(int, input().split())

SA = []
for i in range(S):
    SA.append(input())

TA = []
for i in range(T):
    TA.append(input())

def ok(i, j):
    for x in range(T):
        for y in range(T):
            if SA[i + x][j + y] != TA[x][y]:
                return False
    return True

for i in range(S):
    for j in range(S):
        if i + T > S or j + T > S:
            continue
        if ok(i, j):
            print(i + 1, j + 1)
        


