def solution(my_string, n):
    answer = ''
    
    for i in range(len(my_string)):
        new_string = my_string[i] * n
        answer = answer + new_string
    
    print(answer)
    
    return answer