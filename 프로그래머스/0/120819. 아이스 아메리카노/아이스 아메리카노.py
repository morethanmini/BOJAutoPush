def solution(money):
    answer = []
    
    ice = 5500
    
    cnt = money//ice
    answer.append(cnt)
    
    r = money - (ice * cnt)
    answer.append(r)
    
    return answer