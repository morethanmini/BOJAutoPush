def solution(numbers):
    count = 0
    
    for i in numbers:
        count += i
        
    return count / len(numbers)