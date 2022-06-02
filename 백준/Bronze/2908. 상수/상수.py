a, b = list(input().split())
value_a = int(a[::-1])
value_b = int(b[::-1])

if value_a > value_b:
    print(value_a)
else:
    print(value_b)