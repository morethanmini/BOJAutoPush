import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
    
print(sum(t) - max(t))