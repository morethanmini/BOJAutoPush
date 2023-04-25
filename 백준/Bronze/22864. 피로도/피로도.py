a, b, c, m = map(int, input().split())

hour = 0
tired = 0
work = 0

while hour!=24:
    hour += 1
    
    if tired + a <= m:
        tired += a
        work += b
        
    else:
        if tired > m:
            work = 0
            break
        else:
            tired -= c
            
            if tired < 0:
                tired = 0

print(work)