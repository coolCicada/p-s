N = int(input())
S = input()
T = input()

CNT = 0

for i in range(N):
    if S[i] != T[i]:
        CNT += 1

print(CNT)    