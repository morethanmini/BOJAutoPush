def solution(lottos, win_nums):
    count = 0
    zeros = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    #for i in range(len(lottos)):
    #    if lottos[i] == 0:
    #        zeros += 1
    zeros = lottos.count(0)
    
    #for i in range(len(lottos)):
    #    for j in range(len(win_nums)):
    #        if win_nums[j] == lottos[i]:
    #            count += 1
    for i in lottos:
        if i in win_nums:
            count += 1
    
    answer = rank[count + zeros], rank[count]
    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
#lottos = [0, 0, 0, 0, 0, 0]
#win_nums = [38, 19, 20, 40, 15, 25]
#lottos = [45, 4, 35, 20, 3, 9]
#win_nums = [20, 9, 3, 45, 4, 35]

answer = solution(lottos, win_nums)
print(answer)