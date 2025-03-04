Aq = list(map(int, input().split()))

c = False

for i in range(5):
    if Aq[i] != i + 1 and not c:
        c = True
        temp = Aq[i]
        Aq[i] = Aq[i + 1]
        Aq[i + 1] = temp

T = True

for i in range(5):
    if i + 1 != Aq[i]:
        T = False

print('Yes' if c and T else 'No')