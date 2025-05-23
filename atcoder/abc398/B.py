AS = input().split()
D = {}
for i in AS:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1

DL = D.values()

TWO_C = 0
THREE_C = 0

for i in DL:
    if i >= 2:
       TWO_C += 1
    if i >= 3:
        THREE_C += 1

if TWO_C >= 2 and THREE_C >= 1:
    print('Yes')
else:
    print('No')
        
