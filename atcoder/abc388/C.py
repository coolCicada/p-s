N = int(input())

L = list(map(int, input().split()))

L.sort()

l ,r = len(L) - 1,  len(L) - 1

cnt = 0

while l >= 0:
    if L[l] > L[r] / 2:
        l -= 1
    else:
        cnt += (l + 1)
        r -= 1

print(cnt)
