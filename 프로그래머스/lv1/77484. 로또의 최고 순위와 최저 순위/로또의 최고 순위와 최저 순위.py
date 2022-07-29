def solution(lottos, win_nums):
    count = 0
    zeros = 0
    rank = [6, 6, 5, 4, 3, 2, 1]

    zeros = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            count += 1

    answer = rank[count + zeros], rank[count]
    return answer