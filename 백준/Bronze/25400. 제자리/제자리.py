from collections import deque

n = int(input())
t = list(map(int, input().split()))

dq = deque(t)

cnt = 0
cur = 1

while dq:
    x = dq.popleft()
    if x == cur:
        cur += 1
    else:
        cnt += 1
        
print(cnt)