Q = int(input())

ST = [0] * 100

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 2:
        print(ST.pop())
    else:
        ST.append(query[1])

        