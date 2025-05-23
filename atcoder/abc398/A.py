N = int(input())

if N % 2 == 0:
    N -= 1
    print('-' * (N // 2) + '==' + '-' * (N // 2))
else:
    print('-' * (N // 2) + '=' + '-' * (N // 2))