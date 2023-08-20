# https://www.acmicpc.net/problem/28063

'''
N x N 크기에서
각 꼭짓점 좌표라면 2번
꼭짓점 좌표가 아니라면 3번
1x1 크기의 경우 1번
'''
N = int(input())
x, y = map(int,input().split())
if N==1:
    print(0)
else:
    # 각 꼭짓점에 위치한 좌표라면 2번이 최소
    if (x==1 and y==1) or (x==1 and y==N) or (x==N and y==1) or (x==N and y==N):
        print(2)
    elif x==1 or x==N or y==1 or y==N: # 각 테두리에 위치했다면 3번이 최소
        print(3)
    else: # 안쪽 값이라면 4번이 최소
        print(4)