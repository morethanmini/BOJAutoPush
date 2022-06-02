n = list(map(int, input().split()))
sum = 0

for i in n:
    a = i * i
    sum += a

print(sum%10)