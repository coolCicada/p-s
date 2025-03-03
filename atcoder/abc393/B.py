s = input()

L = len(s)

cnt_r = 0

for i in range(L):
    for j in range(L):
        if j + i >= L or j + i + i >= L:
            break;
        A = s[j]
        B = s[j + i]
        C = s[j + i + i]
        if A == 'A' and B == 'B' and C == 'C':
            cnt_r += 1

print(cnt_r)