# https://www.acmicpc.net/problem/2446
n = int(input())
for i in range(n):
    print(" "*i,end='') # 공백 먼저 출력
    # 별 출력
    print("*"*(2*(n-i)-1),end='')
    print("")
for i in range(2,n+1):
    print(" "*(n-i),end='') # 공백 먼저 출력
    print("*"*(2*i-1),end='')
    print("")