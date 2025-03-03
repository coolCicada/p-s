N, Q = map(int, input().split())

CNT = 0

CN = [1] * (N + 1)
L = list(range(N + 1))

for i in range(Q):
    S = input()
    if S[0] == '1':
        _, F, T = map(int, S.split())
        FL = L[F]
        if CN[FL] == 2:
            CNT -= 1
        if CN[T] == 1:
            CNT += 1

        CN[FL] -= 1
        CN[T] += 1
        L[F] = T
    else:
        print(CNT)