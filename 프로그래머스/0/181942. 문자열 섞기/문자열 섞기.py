def solution(str1, str2):
    answer = ''
    
    for i in range(len(str1)):
        
        str = str1[i]+str2[i]
        answer = answer + str
    
    return answer
