def solution(a, b):
    a, b = str(a), str(b)
    
    w1 = a+b
    w2 = b+a
    
    w1, w2 = int(w1), int(w2)
    
    if w1 > w2:
        answer = w1
    elif w2 > w1:
        answer = w2
    else:
        answer = w1
    

    return answer