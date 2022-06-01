n = int(input())
mirror = []

for _ in range(n):
    value = input()
    mirror.append(value)

s = input()

if s == '1':
    for i in mirror:
        print(i)
elif s == '2':
    for i in mirror:
        print(i[::-1])
else:
    for i in range(-1, -n-1, -1):
        print(mirror[i])