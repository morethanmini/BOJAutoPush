n = int(input())
point = list(map(int, input().split()))
m = max(point)

FakePoint = []
for i in point:
    FakePoint.append(i/m*100)
result = sum(FakePoint)/n
print(result)