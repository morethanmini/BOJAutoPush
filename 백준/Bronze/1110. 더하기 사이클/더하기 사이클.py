N = int(input())

a = N // 10
b = N % 10
i = 0

while True:
    temp = b
    b = (a + b) % 10
    a = temp

    i += 1
    if N == a * 10 + b:
        print(i)
        break