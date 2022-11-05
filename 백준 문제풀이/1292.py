p = []

for i in range(1, 1001):
    for j in range(1, i+1):
        p.append(i)

a, b = map(int, input().split())

sum = 0
for i in range(a-1, b, 1):
    sum += p[i]

print(sum)
