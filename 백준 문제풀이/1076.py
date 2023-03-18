# https://www.acmicpc.net/problem/1076
'''
색	값	곱
black	0	1
brown	1	10
red	2	100
orange	3	1,000
yellow	4	10,000
green	5	100,000
blue	6	1,000,000
violet	7	10,000,000
grey	8	100,000,000
white	9	1,000,000,000

처음 두 색은 값을 이어서 붙이고, 마지막 값은 곱해서 출력한다. 
'''
# 색상에 대한 dict 정의
color = {'black': [0, 1],
         'brown': [1, 10],
         'red': [2, 100],
         'orange': [3, 1000],
         'yellow': [4, 10000],
         'green': [5, 100000],
         'blue': [6, 1000000],
         'violet': [7, 10000000],
         'grey': [8, 100000000],
         'white': [9, 1000000000]}

resistance = []

# 색 3개 입력받기
for _ in range(3):
    resistance.append(input())

# 앞선 색 2개는 이어붙이고, 마지막 색을 곱하여 출력
plus = str(color[resistance[0]][0])+str(color[resistance[1]][0])
result = int(plus) * color[resistance[2]][1]

print(result)
