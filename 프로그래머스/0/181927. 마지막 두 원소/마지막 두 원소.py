def solution(num_list):
    
    if num_list[-1:][0] > num_list[-2:-1][0]:
        num_list.append(num_list[-1:][0] - num_list[-2:-1][0])
    else:
# num_list[-2:-1][0] > num_list[-1:][0]:
        num_list.append(num_list[-1:][0] * 2)
        
    return num_list