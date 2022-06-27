t = int(input())

for i in range(1, t+1):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]

    for j in range(k):
        for q in range(1, n):
            people[q] += people[q-1]

    print(people[-1])