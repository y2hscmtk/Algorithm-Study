# https://www.acmicpc.net/problem/20438
import sys
input = sys.stdin.readline
# 학생의 수 N, 졸고 있는 학생의 수 K, 지환이가 출석 코드를 보낼 학생의 수 Q, 주어질 구간의 수 M
n, k, q, m = map(int, input().split())

sleep = [0]*(n+3)  # 자는사람
check = [0]*(n+3)  # 출석체크 한사람
# 자는사람 기록
for i in map(int, input().split()):
    sleep[i] = 1
# 출석체크
for i in map(int, input().split()):
    # 졸고 있는 학생들은 출석 코드를 제출하지 않고, 다른 학생들에게 보내지 않는다.
    if sleep[i]:
        continue  # 자고 있다면 출석체크 불가능
    # i의 배수한테 출석체크 문자 보내기
    for j in range(i, n+3, +i):
        if not sleep[j]:  # 자고 있지 않다면
            check[j] = 1  # 출석체크 가능

# 각 구간별로 출석체크 한 사람 구하기(누적합 배열 작성)
pSum = [0]*(n+3)
for i in range(3, n+3):  # 3번부터 확인(3번 부터 시작임)
    pSum[i] = pSum[i-1] + check[i]

# 입력받은 구간에 맞춰 정답 출력
for _ in range(m):
    start, end = map(int, input().split())
    # 구간내 학생 수에서, 출석체크 한 인원을 빼면 => 출석이 되지 않은 학생 수(정답)
    people = end-start+1
    print(people - (pSum[end] - pSum[start-1]))
