class UF:
    def __init__(self):
        self.parent = list(range(0, N + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if x > y:
            x, y = y, x
        self.parent[x] = y
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

N, M = map(int, input().split())

CS = [0] * M
for i in range(M):
    CS[i] = list(map(int, input().split()))
    
UFO = UF()

R = 0

for i in range(M):
    if not UFO.connected(CS[i][0], CS[i][1]):
        UFO.union(CS[i][0], CS[i][1])
    else:
        R += 1
        
print(R)
    
