arr = ['1','2','3','4','5','6','7','8']

v = list(input().split())

if v == arr[:]:
    print("ascending")
elif v == arr[::-1]:
    print("descending")
else:
    print("mixed")