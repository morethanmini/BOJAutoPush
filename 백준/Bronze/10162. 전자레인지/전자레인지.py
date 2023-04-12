n = int(input())
t = [300, 60, 10]


if n%10 != 0:
	print(-1)
else:
	for i in t:
		print(n//i, end=' ')
		n%=i