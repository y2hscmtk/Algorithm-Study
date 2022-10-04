# https://www.acmicpc.net/problem/11000

'''
강의실 배정

수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!
'''
import sys
import heapq

n = int(input())

data = []
h = []


for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort()  # 오름차순 정렬

# class_room.append(data[0])  # 리스트 형태로 첫번째 수업 삽입
# for i in range(1, len(data)):
#     flag = False
#     for j in range(len(class_room)):
#         if data[i][0] >= class_room[j][1]:  # 같은 방에 넣을 수 있는 수업일 경우
#             class_room[j][1] = data[i][1]  # (1,2) (2,4) => (1,4)의 형태로 저장
#             flag = True  # 기존 방에 합치기 성공
#             break
#     if flag == False:  # 합치기 실패의 경우
#         class_room.append(data[i])  # 새로 방을 만들어 삽입

# print(len(class_room))  # 방의 개수를 출력

# 시간초과 문제를 해결하기 위해 heapq를 사용해야함
for i in range(n):
    if len(h) != 0 and h[0] <= data[i][0]:  # 붙일수 있는 수업이라면
        heapq.heappop(h)  # 기존의 가장 작은 끝나는 수업 제거
    heapq.heappush(h, data[i][1])  # 새롭게 붙일 수업의 끝나는시간 삽입

print(len(h))  # 히프에 남아있는 것들은 한 방을 사용하는 클래스의 수
