'''
(M = 10,N = 12)
Year 11 : <1:11>
x = 1, y = 11

Year 12
x = 1, y = 11
x' = x + 1 (x<m이므로)
y' = y + 1 (y<n이므로)
= <2:12>

Year 13
x = 2, y = 12
x' = x + 1 (x<m)
y' = 1 (y>=n)
= <3:1>

브루트포스기법으로 끝에 도달할때까지 모든 경우에 대해서 공식 적용?
카잉달력의 마지막에 도달하였을 때에 종료
'''
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    m,n,x,y = map(int,input().split())
    find = False
    nx,ny,year = 1,1,1 # 첫번째 해는 <1:1>로 표현된다.
    while True:
        if (nx,ny) == (x,y):
            find = True
            print(year)
            break
        if (nx,ny) == (m,n):
            break
        # 공식 적용 - 브루트포스
        if nx<m:
            nx += 1
        else:
            nx = 1
        if ny<n:
            ny += 1
        else:
            ny = 1
        year += 1
    if not find:
        print(-1)   