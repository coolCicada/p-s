N = int(input())
AS = list(map(int, input().split()))

mp = set()
cnt = 0

ASP = [0] * N
for index, item in enumerate(AS):
    if item not in mp:
        mp.add(item)
        cnt += 1
    ASP[index] = cnt
    
ASA = [0] * N
AS = AS[::-1]
mp = set()
cnt = 0
for index, item in enumerate(AS):
    if item not in mp:
        mp.add(item)
        cnt += 1
    ASA[index] = cnt

ASA = ASA[::-1]
mx = 0
for i in range(N - 1):
    mx = max(mx, ASP[i] + ASA[i + 1])
    
print(mx)