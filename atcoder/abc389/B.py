N = int(input())

t = 1

for i in range(1, N + 1):
    t *= i
    if t == N:
        print(i)
        exit(0)