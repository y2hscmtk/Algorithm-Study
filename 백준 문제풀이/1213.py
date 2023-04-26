# https://www.acmicpc.net/problem/1213
import sys
# 초기 문자 입력받기
data = list(input())

# 정답이 여러개 일때는 사전순으로 앞에 나가는것을 출력한다.
data.sort()

# 먼저 전체 알파벳 개수를 파악한다. dict이용
dict = {}
for a in data:
    # 처음 기록되는 알파벳이라면 1로 초기화
    if a not in dict:
        dict[a] = 1  # 개수 세기
    else:  # 기존에 있는 알파벳이라면 +1
        dict[a] += 1

p = []
error_count = 0  # 홀수개인 단어가 몇개인지 확인하는 용
last = []
# 딕셔너리에서 키 하나씩 뽑으면서 배치하기(왼쪽에 절반만 배치)
for alpha in dict:
    # 팰린드롬에 단어 배치
    # 짝수개인지 홀수개인지 확인
    if dict[alpha] % 2 != 0:
        last.append(alpha)  # 마지막에 올 단어 하나 삽입
        error_count += 1  # 홀수개일경우 에러카운트 증가
    # 짝수든 홀수든 절반만큼 배치
    n = dict[alpha]//2
    p.append(alpha*n)  # 절반만큼 배치
# 서로 다른 문자일때만 에러카운트가 증가하므로
    # 에러카운트가 2개 이상이라면 => 펠린드롬을 완성할수 없음
if error_count >= 2:
    print("I'm Sorry Hansoo")  # 미안하게 됐수다
    sys.exit(0)  # 프로그램 종료


for a in p:
    print(a, end='')
if len(last) != 0:
    print(last[0], end='')
for a in range(len(p)-1, -1, -1):
    print(p[a], end='')
