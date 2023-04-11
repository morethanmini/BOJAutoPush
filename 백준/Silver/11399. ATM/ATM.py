n = int(input())
seq = list(map(int, input().split()))
seq.sort()

sum = 0
time = []

for i in seq:
    sum += i
    time.append(sum)

count = 0

for j in time:
    count += j

print(count)