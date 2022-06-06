n, m = map(int, input().split())
num = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            card_num = num[i] + num[j] + num[k]

            if card_num <= m:
                result = max(result, card_num)

print(result)