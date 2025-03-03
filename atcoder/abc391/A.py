'''
North: N
East: E
West: W
South: S
Northeast: NE
Northwest: NW
Southeast: SE
Southwest: SW
'''
D = input()
Arr = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E'
}

if len(D) == 1:
    print(Arr[D])
else:
    print(f'{Arr[D[0]]}{Arr[D[1]]}')
