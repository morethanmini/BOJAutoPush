def solution(a, b):
    sa, sb = str(a), str(b)
    
    w1 = int(sa+sb)
    w2 = 2 * a * b
    
    if w1 > w2:
        answer = w1
    elif w2 > w1:
        answer = w2
    else:
        anser = w1
    
    return answer