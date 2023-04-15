# https://www.acmicpc.net/problem/2108
from collections import Counter
import sys
input = sys.stdin.readline
data = []
n = int(input())
for _ in range(n):
    data.append(int(input()))

'''
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.
'''

s = sum(data)
print(round((s/n)))

data.sort()
print(data[(n-1)//2])

# 최빈값 계산 => 가장 많이 등장하는 값
dict = {}
for d in data:
    if d not in dict:
        dict[d] = 1
    else:
        dict[d] += 1

array = []
mx = max(dict.values())  # 값들중 최고 등장횟수 기록
for d in dict:
    if dict[d] == mx:  # 최고등장횟수와 같다면
        array.append(d)  # 삽입

if len(array) > 1:  # 1개 이상이라면
    print(array[1])  # 2번째 값 출력
else:
    print(array[0])


# 범위 최대값과 최소값의 차이
print(max(data)-min(data))
