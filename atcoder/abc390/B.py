N = int(input())

L = list(map(int, input().split()))
L.sort()

R = sum(L[:-1])
print('Yes' if R > L[-1] else 'No')