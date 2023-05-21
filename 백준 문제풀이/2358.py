# https://www.acmicpc.net/problem/2358
'''
하나의 좌표가 일치한다면 => 직선을 그을수 있다.
즉 x,y에 평행하는 한 직선에 대해서, 해당 직선에 포함되는 점이 '2개 이상' 있는지 확인하여
조건을 만족한다면 그 직선을 카운팅한다.
x축에 평행한 직선과 y축에 평행한 직선 둘 다 만족해야하므로
x[] 와 y[] 를 만들어서 좌표별로 몇개씩 있는지 확인한다.
예를 들어 [[0,0],[10,10],[0,10],[10,0]] 의 경우
x[0] = 2, x[10] = 2, y[0] = 2, y[10] = 2 가 되며, 모두 2 이상이므로 4개의 직선이 그어지게 된다.
'''
# 각 좌표에 해당하는 점이 몇개인지 카운팅 하기 위해
dict_x = {}
dict_y = {}
# px = [0]*100001
# py = [0]*100001

for _ in range(int(input())): # n만큼 데이터 입력받기
    x,y = map(int,input().split())
    # 각 좌표 카운트 증가
    if x not in dict_x:
        dict_x[x] = 1
    else:
        dict_x[x] += 1
    if y not in dict_y:
        dict_y[y] = 1
    else:
        dict_y[y] += 1

count = 0
for key in dict_x:
    if dict_x[key] >=2:
        count+=1
for key in dict_y:
    if dict_y[key] >=2:
        count+=1
print(count)