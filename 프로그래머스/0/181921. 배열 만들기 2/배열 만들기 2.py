def solution(l, r):
    answer = []
    temp = [-1]
    
    for i in range(l, r+1):
        
        i = str(i)
        answer.append(i)
        
    filtered_lst = [x for x in answer if set(x) <= {"0", "5"}]
    
    int_lst = [int(x) for x in filtered_lst]
    int_lst.sort()
    
    if int_lst:
        return int_lst
    else:
        return temp

