N, M = map(int, input().split())

T = 0

for i in range(M + 1):
    T += N ** i
    if T > 10 ** 9:
        print('inf')
        exit(0)
    
print(T)