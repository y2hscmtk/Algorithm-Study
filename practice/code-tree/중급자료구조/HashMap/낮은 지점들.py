# HashMap / 낮은 지점들
'''
2차 평면 위에 n개의 점이 주어졌을 때,
동일한 x좌표를 갖는 점들에 대해서는 그 중 가장 작은 y값을 갖는 점을 제외한 다른 점들은 전부 제거하여 
하나의 x좌표 당 최대 하나의 점만 놓여져 있도록 만들려고 합니다. 
이후 남아있는 점들의 y값의 합을 구하는 프로그램을 작성해보세요.
'''
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

point_dict = dict()

result = 0
for x,y in points:
    if x in point_dict:
        point_dict[x] = min(point_dict[x], y) # 더 작은 값으로 업데이트
    else:
        point_dict[x] = y

# 남아있는 y좌표 합 계산
for x in point_dict:
    result += point_dict[x]

print(result)