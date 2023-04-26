from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
que = []

for i in range(n):
    t = input().split()
    
    if t[0] == 'push':
        que.insert(0, t[1])
    
    elif t[0] == 'pop':
        if len(que) != 0:
            print(que.pop())
        else:
            print(-1)
    
    elif t[0] == 'size':
        print(len(que))
        
    elif t[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
            
    elif t[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[len(que) - 1])
    
    elif t[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])