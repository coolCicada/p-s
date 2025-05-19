N = int(input())
nums = list(map(int, input().split()))

mp = {}

r = float('inf')

for i in range(N):
    if nums[i] in mp:
       r = min(i - mp[nums[i]] + 1, r)
    mp[nums[i]] = i 

print(r if r != float('inf') else -1)
    