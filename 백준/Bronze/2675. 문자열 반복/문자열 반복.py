t = int(input())

for i in range(1, t+1):
    num, word = input().split()
    text = ''

    for j in word:
        text += int(num) * j
    print(text)