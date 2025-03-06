N = int(input())

L = list(map(int, input().split()))

for i in range(2, len(L)):
    if L[i - 1] * L[i - 1] != L[i - 2] * L[i]:
        print('No')
        break;
else:
    print('Yes')