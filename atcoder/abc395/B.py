N = int(input())

arr = [['#'] * N for i in range(N)]

for i in range(N):
    for j in range(N):
        if (min(i, j, N - 1 - j, N - 1 - i) % 2 == 0):
            arr[i][j] = '#'
        else:
            arr[i][j] = '.'
            
for i in range(N):
    print(''.join(arr[i]))