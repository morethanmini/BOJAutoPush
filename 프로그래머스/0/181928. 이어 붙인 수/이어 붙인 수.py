def solution(num_list):
    arr1 = []
    arr2 = []
    
    for i in num_list:
        if i % 2 == 0:
            arr1.append(i)
        else:
            arr2.append(i)
            
    s1 = ''.join(map(str, arr1))
    s2 = ''.join(map(str, arr2))
    
    return int(s1) + int(s2)