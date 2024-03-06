def solution(num_list):
    answer = []
    
    jjack = 0
    hol = 0
    
    for i in num_list:
        if i % 2 ==0:
            jjack += 1
            
        else:
            hol += 1
            
    answer.append(jjack)
    answer.append(hol)
    
    return answer