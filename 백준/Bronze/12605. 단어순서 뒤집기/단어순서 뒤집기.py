t = int(input())

for i in range(1, t+1):
    n = list(input().rstrip().split())
    print("Case #{}: {}".format(i, ' '.join(n[::-1])))