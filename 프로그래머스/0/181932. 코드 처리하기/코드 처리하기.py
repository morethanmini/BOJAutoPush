def solution(code):
    
    answer = ''
    mode = 0
    
    
    for i in range(len(code)):
        if code[i] == '1':
            mode = 1 - mode
        
        if mode == 0:
            if i % 2 == 0:
                if code[i] == '1':
                    continue
                else:
                    answer += code[i]
        
        if mode == 1:    
            if i % 2 != 0:
                if code[i] == '1':
                    continue
                else:
                    answer += code[i]
    if not answer:
        return 'EMPTY'
    
    return answer