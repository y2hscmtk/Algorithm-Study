# https://www.acmicpc.net/problem/10811
n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    data[s-1:e] = data[s-1:e][::-1]
print(*data)
