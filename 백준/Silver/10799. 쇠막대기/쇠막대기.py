t = input()
stack = []
cnt = 0

for i in range(len(t)):
    if t[i]=='(':
        stack.append(t[i])
    else:
        if t[i-1]=='(':
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1
            
print(cnt)