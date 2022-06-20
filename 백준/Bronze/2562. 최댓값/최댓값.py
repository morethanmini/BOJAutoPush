arr = []

for i in range(1,10):
    n = int(input())
    arr.append(n)

max = max(arr)
print(max)
print(arr.index(max)+1)