def solution(progresses, speeds):
    answer = []  # 배포될 작업 수를 저장할 리스트
    days_left = []  # 각 작업이 완료되기까지 남은 일수를 저장할 리스트
    
    # 각 작업의 개발 완료까지 남은 일수 계산
    for progress, speed in zip(progresses, speeds):
        days = (100 - progress) // speed
        if (100 - progress) % speed != 0:
            days += 1
        days_left.append(days)
    
    # 배포될 작업 수 계산
    count = 1
    max_day = days_left[0]
    for i in range(1, len(days_left)):
        if days_left[i] <= max_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_day = days_left[i]
    answer.append(count)  # 마지막 배포될 작업 수 추가
    
    return answer