# https://www.acmicpc.net/problem/2522

n = int(input())

for i in range(n, 0, -1):
    print(" "*(i-1), end='')
    print("*"*(n-(i-1)))
for i in range(n-1, 0, -1):
    print(" "*(n-i), end='')
    print("*"*i)
