def solution(my_string):
    answer = []

    for char in my_string:
        if char.isdigit():
            answer.append(char)
    
    answer.sort()
    
    answer = [int(x) for x in answer]

    return answer