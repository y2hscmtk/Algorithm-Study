# 시간초과 판정 방지
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

# 비교연산의 속도를 높이기 위해 집합 자료구조 이용
arrayA = set()

for i in range(n):
    arrayA.add(input())

count = 0

# 입력과 동시에 기존배열에 값이 존재하는지 탐색
for j in range(m):
    data = input()
    if data in arrayA:
        count+=1

# 정답 출력
print(count)
