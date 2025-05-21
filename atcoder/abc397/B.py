S = input()

r = 0

curr = 'i'

index = 0

while index < len(S):
    if S[index] != curr: 
        r += 1
    else:
        index += 1
    curr = 'o' if curr == 'i' else 'i'
    
print(r if curr == 'i' else r + 1)