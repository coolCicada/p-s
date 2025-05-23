N = int(input())

PS = list(map(int, input().split()))
PS_INDEX = list(range(0, N))

PS_INDEX.sort(key=lambda x: PS[x], reverse=True)

R = [1] * N

r = 1

R[PS_INDEX[0]] = r

for i in range(1, N):
    r += 1
    if PS[PS_INDEX[i]] == PS[PS_INDEX[i - 1]]:
        R[PS_INDEX[i]] = R[PS_INDEX[i - 1]]
    else:
        R[PS_INDEX[i]] = r

    
for i in range(N):
    print(R[i])