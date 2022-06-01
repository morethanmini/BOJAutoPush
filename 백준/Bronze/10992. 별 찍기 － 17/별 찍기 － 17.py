N = int(input())

for i in range(1, N+1):
    if i == 1:  # 첫 번째 줄
        print(' ' * (N - i) + "*")

    elif i == N:  # 마지막 줄
        print("*" * (i * 2 - 1))

    else:  # 중간
        print(' ' * (N - i) + "*" + ' ' * (i * 2 - 3) + "*")