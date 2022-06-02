t = int(input())

for _ in range(1, t+1):
    num, word = input().split()
    text =''

    for i in word:
        text += int(num) * i
    print(text)