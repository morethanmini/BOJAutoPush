n = int(input())

count = 0

for i in range(1, n+1):
    if n>=0:
        n -= i
        
        if n>=0:
            count += 1
    
    if n < 0:
        break

print(count)