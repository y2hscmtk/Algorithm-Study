# https://www.acmicpc.net/problem/1620
import sys
input = sys.stdin.readline

name2num = {}
num2name = {}


n, m = map(int, input().split())
for i in range(n):
    name = input().rstrip()
    name2num[name] = (i+1)
    num2name[i+1] = name

# m개의 줄에 맞춰야 할 질문이 입력된다.
# 번호를 입력받으면 포켓몬을,
# 포켓몬을 입력받으면 번호를 출력한다.
for i in range(m):
    query = input().rstrip()
    # isdigit를 이용하여, 입력이 전부 숫자인지 확인 할 수 있음
    if query.isdigit():
        # 입력이 숫자인 경우
        num = int(query)
        print(num2name[num])
    else:
        # 입력이 문자열인 경우
        name = query
        print(name2num[name])
