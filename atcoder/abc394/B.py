N = int(input())
arr = []
for i in range(N):
    arr.append(input())

arr.sort(key = len)
print(''.join(arr))