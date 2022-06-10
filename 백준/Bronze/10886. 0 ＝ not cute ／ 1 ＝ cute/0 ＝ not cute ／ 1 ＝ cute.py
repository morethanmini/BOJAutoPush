n = int(input())
c, nc = 0, 0

for i in range(n):
    v = int(input())

    if v == 1:
        c += 1
    else:
        nc += 1

if c > nc:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')