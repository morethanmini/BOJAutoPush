n = int(input())

level_score = []
cnt = 0

for _ in range(n):
    level_score.append(int(input()))
    
for i in range(n-1, 0, -1):
    if level_score[i] <= level_score[i-1]:
        cnt += (level_score[i-1] - level_score[i]) + 1
        level_score[i-1] = level_score[i] - 1
        
print(cnt)