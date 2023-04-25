n = int(input())

stack = []

for i in range(n):
    t = int(input())

    if t!=0:
        stack.append(t)

    elif t==0:
        stack.pop()
        
print(sum(stack))