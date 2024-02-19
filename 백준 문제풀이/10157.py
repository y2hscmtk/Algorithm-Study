# https://www.acmicpc.net/problem/10157
'''
구현, 브루트포스
최악의 경우에도 1000000번의 반복문
왼쪽 아래를 왼쪽 위로 생각하여 오른쪽으로 90도 회전해서 생각(우리에게 익숙한 배열의 형태)
(0,0),(0,1),(0,2),(0,3)..(0,c-1)
(1,0),(1,1),(1,2),(1,3)..(1,c-1)
(2,0),(2,1),(2,2),(2,3)..(2,c-1)
.................................
(r-1,0),(r-1,1),(r-1,2)..(r-1,c-1)
'''
c,r = map(int,input().split()) # c는 가로, r는 세로
k = int(input())
if k>c*r:
    print(0)
else:
    x,y,t,i = 1,1,1,3 # i는 현재 이동방향
    min_x,max_x,min_y,max_y = 1,c,1,r
    # 시계방향 이동 설정
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    count = 0
    while True:
        # 기준점 바꿔야 되는지 확인
        if count == 4 and (x,y) == (min_x,min_y):
            count = 0
            min_x+=1;min_y+=1
            max_x-=1;max_y-=1
            x,y = min_x,min_y
        if t==k:
            print(x,y)
            break
        if (x,y) == (min_x,min_y): # 왼쪽 위
            i+=1
            count+=1
        elif (x,y) == (min_x,max_y): # 오른쪽 위
            i+=1
            count+=1
        elif (x,y) == (max_x,max_y): # 오른쪽 아래
            i+=1
            count+=1
        elif (x,y) == (max_x,min_y): # 왼쪽 아래
            i+=1
            count+=1
        i%=4
        x += dx[i]
        y += dy[i]
        t+=1
        