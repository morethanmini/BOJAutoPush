import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    t = int(input())
    
    while stack and stack[-1]<=t:
        stack.pop()
    
    stack.append(t)

print(len(stack))