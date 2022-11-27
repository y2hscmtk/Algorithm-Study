# https://www.acmicpc.net/problem/11651

'''
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, 
y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''

'''
아이디어 람다식을 이용하여 정렬의 기준을 정하면 될듯하다.
'''

n = int(input())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))


# 가장 마지막 조건을 대상으로 먼저 정렬해야 원하는 정렬이 이뤄진다.
data = sorted(data, key=lambda x: x[0])  # 먼저 x좌표가 증가하는 순으로 정렬한뒤
data = sorted(data, key=lambda x: x[1])  # y좌표를 우선기준으로 재정렬


for x, y in data:
    print(x, y)
