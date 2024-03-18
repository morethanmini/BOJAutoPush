def solution(t, p):
    answer = 0
    arr = []
        
    for i in range(len(t)):
        segments = t[i:i+len(p)]
        
        if len(segments) == len(p):
            arr.append(segments)
        
    for i in arr:
        if i <= p:
            answer += 1
    
    return answer