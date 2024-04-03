# https://www.acmicpc.net/problem/2477
'''
어차피 육각형으로 고정되어 있음
동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4인 상황이므로, (1,2)중 최대 값이 큰 사각형의 가로, (3,4)중 최대 값이 큰 사각형의 세로에 해당한다.
큰 사각형의 세로 * 가로를 통해 큰 사각형의 넓이를 구하고, 작은 사각형의 넓이를 빼고, 참외의 개수만큼 곱해서 답을 구한다.

가장 큰 가로는 두 값의 비교로 정의가 가능하나, 들어가는 사각형의 경우, 어떤 값이 작은 사각형의 가로 변이 되는 지 알 수 없다.
(입력받은 다른 가로 값, 혹은 큰 가로-입력받은 다른 가로 값)

길이가 짧은 세로 값의 왼쪽 오른쪽 값 중 작은 값이 들어가는 사각형의 가로 값이 된다.

'''
import sys
k = int(input())
max_x,min_x,max_y,min_y = 0,sys.maxsize,0,sys.maxsize
data = []
for i in range(6): # 육각형의 모든 면에 대한 정보
    d,length = map(int,input().split())
    data.append(length)
    if d in [3,4]: # 세로 대한 정보라면
        if max_y < length:
            max_y = length # 가장 큰 세로 갱신
            height_index = i # 가장 큰 세로의 인덱스 저장
    elif d in [1,2]: # 가로에 대한 정보라면
        if max_x < length:
            max_x = length # 가장 큰 가로 갱신
            length_index = i # 가장 큰 가로의 인덱스 저장

# 들어가는 사각형에 대한 정보
# 1. 가장 큰 가로의 양 옆 값을 비교 => 두 값 중 작은 값이 들어가는 사각형의 이전 세로 값에 해당
temp_length = data[length_index-1] if data[length_index-1] < data[(length_index+1)%6] else data[(length_index+1)%6]
min_y = max_y-temp_length # 그 값을 뺀 값이 들어가는 사각형의 세로
# 2. 가장 큰 세로의 양 옆 값을 비교 => 두 값 중 작은 값이 들어가는 사각형의 이전 가로 값에 해당
temp_height = data[height_index-1] if data[height_index-1] < data[(height_index+1)%6] else data[(height_index+1)%6]
min_x = max_x-temp_height # 그 값을 뺀 값이 들어가는 사각형의 가로

print(k*((max_x*max_y)-(min_x*min_y)))
