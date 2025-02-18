def solution(a, b, c):
    if (a != b) and (a != c) and (b != c):
        return a+b+c
    
    if (a == b) and (a != c):
        return (a+b+c) * (a*a + b*b + c*c)
    
    if (a == c) and (b != c):
        return (a+b+c) * (a*a + b*b + c*c)
    
    if (b == c) and (a != c):
        return (a+b+c) * (a*a + b*b + c*c)
    
    if a == b == c:
        return (a+b+c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)