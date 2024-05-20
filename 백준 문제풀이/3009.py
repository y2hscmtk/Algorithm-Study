# https://www.acmicpc.net/problem/3009
first, second = [],[]
result = [0,0]
for _ in range(3):
    a,b = list(map(int,input().split()))
    first.append(a); second.append(b)
for f in first:
    if first.count(f) == 1:
        result[0] = f
for s in second:
    if second.count(s) == 1:
        result[1] = s
print(*result)