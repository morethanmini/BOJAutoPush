def solution(num_list):
    m = 1
    
    for i in num_list:
        m = m * i
    
    if m < sum(num_list) * sum(num_list):
        return 1
    else:
        return 0
        