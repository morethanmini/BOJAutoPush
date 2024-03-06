def solution(n, k):
        
    if n < 10:
        sheep = n * 12000
        drink = k * 2000
        answer = sheep + drink
    
    else:
        sheep = n * 12000
        drink = (k * 2000) - ((n//10) * 2000) 
        answer = sheep + drink
    
    return answer