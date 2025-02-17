def solution(n):
    answer = 0
    arr = []
    
    if n % 2 == 0:
        for i in range(1, n+1):
            if i % 2 == 0:
                arr.append(i)
                
        for j in arr:
            q = j * j
            answer = answer + q
    else:
        for i in range(1, n+1):
            if i % 2 !=0:
                arr.append(i)
                answer = sum(arr)

    
    return answer