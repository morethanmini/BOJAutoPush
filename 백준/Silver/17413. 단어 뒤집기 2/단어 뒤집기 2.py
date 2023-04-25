s = input()

temp = []
stack = []

for i in range(len(s)):
    if s[i]=='>':
        temp.append('>')
        stack.append(''.join(temp))
        temp = []
        
    elif s[i]=='<' and temp:
        temp.reverse()
        stack.append(''.join(temp))
        temp = [s[i]]
    
    elif s[i]==' ' and '<' not in temp:
        temp.reverse()
        stack.append(''.join(temp))
        stack.append(' ')
        temp = []
        
    else:
        temp.append(s[i])

if temp:
    temp.reverse()
    stack.append(''.join(temp))
    
print(''.join(stack))