# https://www.acmicpc.net/problem/10808
dict = {}
# 딕셔너리 초기화
for alph in "abcdefghijklmnopqrstuvwxyz":
    dict[alph] = 0

# 입력받은 문자열로부터 문자 개수 카운팅
for alph in input():
    dict[alph] += 1

# 정답 출력
for key in dict:
    print(dict[key], end=' ')
