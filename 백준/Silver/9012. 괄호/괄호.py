n = int(input())

for _ in range(n):
    t = input()
    stack = []
    
    for i in t:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                stack.append(i)
                break
            else:
                stack.pop()
        
    if not stack:
        print('YES')
    else:
        print('NO')