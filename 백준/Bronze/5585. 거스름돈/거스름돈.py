n = int(input())

coins = [500, 100, 50, 10, 5, 1]

num = 1000 - n
count = 0

for coin in coins:
    if num >= coin:
        count += num//coin
        num %= coin
    
    if num <= 0:
        break
    
print(count)