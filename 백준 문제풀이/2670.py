# https://www.acmicpc.net/problem/2670
'''
문제
N개의 실수가 있을 때, 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아, 그 곱을 출력하는 프로그램을 작성하시오. 
예를 들어 아래와 같이 8개의 양의 실수가 주어진다면,
1.1/0.7/[1.3/0.9/1.4]/0.8/0.7/1.4
색칠된 부분의 곱이 최대가 되며, 그 값은 1.638이다.
'''
n = int(input())

# 실수 입력받기
number = []
for i in range(n):
    number.append(float(input()))


result = -1  # 최대값을 저장하기 위해


# 구간을 달리하면서 dp에 값을 저장하고
# 쵀대값을 갱신해주면 될듯

# # 시작 구간
# for i in range(n):
#     for j in range(i,n):
