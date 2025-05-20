N, M = map(int, input().split())
BL = list(map(int, input().split()))
ML = list(map(int, input().split()))

BL.sort(reverse=True)
ML.sort(reverse=True)

for i in range(1, N):
    BL[i] += BL[i - 1]

for i in range(1, M):
    ML[i] += ML[i - 1]
    
for i in range(N - 2,-1, -1):
    BL[i] = max(BL[i], BL[i + 1])
    
mx = max(max(BL), 0)

for i in range(min(N, M)):
    mx = max(mx, BL[i] + ML[i])
    
print(mx)