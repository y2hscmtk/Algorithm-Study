# https://www.acmicpc.net/problem/2445

n = int(input())

for i in range(1, n):
    print("*"*i, end='')
    print(" "*((n*2)-(i*2)), end='')
    print("*"*i)
print("*"*(n*2))
for i in range(n-1, 0, -1):
    print("*"*i, end='')
    print(" "*((n*2)-(i*2)), end='')
    print("*"*i)
