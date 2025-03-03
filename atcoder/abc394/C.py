arr = list(input())
n = len(arr)
for i in range(n - 2, -1, -1):
    if (arr[i] == 'W' and arr[i + 1] == 'A'):
        arr[i] = 'A'
        arr[i + 1] = 'C'
print(''.join(arr))