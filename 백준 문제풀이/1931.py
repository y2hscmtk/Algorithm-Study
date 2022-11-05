# 백준 1931번 재도전
# https://www.acmicpc.net/problem/1931

'''
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 
만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 
회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
'''

'''
아이디어
그리디 알고리즘 원칙에 따라
수업이 짧게 끝나고, 일찍 시작하는 수업을 골라 차례로 넣는다.
'''

n = int(input())
data = []  # 수업의 시작시간과 끝시간을 각각 저장할 리스트

for _ in range(n):
    data.append(list(map(int, input().split()),))

# 수업시간이 짧고, 수업이 일찍 시작하는 순서대로 배열 재정렬
data.sort(key=lambda x: x[0])  # 2차적으로 수업시작시간이 작은 순대로 정렬시킨다.
sorted_list = sorted(data, key=lambda x: x[1])  # 총 수업시간이 작은 순대로 데이터를 정렬시킨다.

c = []  # 수업
c.append(sorted_list[0])
for i in range(1, n):
    if c[-1][1] <= sorted_list[i][0]:  # 이전 수업시간 이후에 수업이 시작하는지 확인
        c.append(sorted_list[i])

print(len(c))
