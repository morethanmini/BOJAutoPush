c = int(input())

for i in range(1, c+1):
    n = list(map(int, input().split()))
    c = 0

    for j in n[1:]:
        avg = sum(n[1:]) / n[0]

        if j > avg:
            c += 1

    result = c / n[0] * 100
    print('{0:0.3f}%'.format(result))