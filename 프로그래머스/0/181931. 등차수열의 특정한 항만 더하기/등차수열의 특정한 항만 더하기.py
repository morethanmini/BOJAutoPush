def solution(a, d, included):
    sum = 0
    
    for i in included:
        if i == True:
            sum += a
        a += d
    
    return sum