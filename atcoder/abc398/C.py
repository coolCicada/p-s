N = int(input())
AS = list(map(int, input().split()))

AST = list(range(N))

AST.sort(key = lambda x: AS[x], reverse=True)

R = -1

for i in range(N - 1):
    if i == 0 and AS[AST[i]] != AS[AST[i + 1]] or i > 0 and AS[AST[i]] != AS[AST[i + 1]] and AS[AST[i - 1]] != AS[AST[i]]:
        R = AST[i]
        print(R + 1)
        exit(0)
if N == 1:
    print(1)
    exit(0)
    
if AS[AST[N - 1]] != AS[AST[N - 2]]:
    R = AST[N - 1]
print(R + 1 if R != -1 else -1)
    

