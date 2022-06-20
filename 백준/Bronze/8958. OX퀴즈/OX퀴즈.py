T = int(input())

for i in range(1, T+1):
    quiz = list(input())
    point = 0
    sum = 0

    for j in quiz:
        if j == 'O':
            point += 1
            sum += point
        else:
            point = 0

    print(sum)