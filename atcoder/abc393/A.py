a, b = input().split()
if a == 'fine' and b == 'fine':
    print('4')
elif a == 'sick' and b == 'sick':
    print('1')
elif a == 'sick' and b == 'fine':
    print('2')
else:
    print('3')