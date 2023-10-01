# https://www.acmicpc.net/problem/4153
'''
피타고라스 정의를 통해 확인해보기
a,b,c a<c, b<c 일때 a^2 + b^2 = c^2 를 만족하면 직각삼각형
'''
while True:
    data = sorted(list(map(int,input().split())))
    if data[0] == 0:
        break
    if data[0]**2 + data[1]**2 == data[2]**2:
        print("right")
    else:
        print("wrong")