a = input().upper()
b = list(range(ord("A"), ord("Z")+1))
arr = []

for i in b:
    arr.append(a.count(chr(i)))

if arr.count(max(arr)) > 1:
    print("?")
else:
    print(chr(b[arr.index(max(arr))]))