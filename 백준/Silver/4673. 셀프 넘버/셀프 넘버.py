n = set(range(1, 10001))
s_n = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    s_n.add(i)

result = sorted(n - s_n)

for i in result:
    print(i)