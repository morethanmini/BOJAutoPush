n = int(input())

if n % 2 == 0:
    print('1 2 ' * (n//2))
else:
    print('1 2 ' * (n//2), '3', sep='')