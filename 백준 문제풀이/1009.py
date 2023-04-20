# https://www.acmicpc.net/problem/1009
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(str(a**b)[-1])
