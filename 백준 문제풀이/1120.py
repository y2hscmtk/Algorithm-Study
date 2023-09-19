# https://www.acmicpc.net/problem/1120

'''
A의 앞에 아무 알파벳이나 추가한다.
A의 뒤에 아무 알파벳이나 추가한다.
'''
import sys
a, b = input().split()

result = sys.maxsize


def dfs(a):
    global result
    # 길이가 같아지기 전까지 연산 수행
    if len(a) == len(b):
        # 두 문자열 간의 차이가 몇인지 계산하여 갱신
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1  # 불일치 글자 +1
        # 정답 갱신
        result = min(result, count)
        return
    # 앞에 붙이거나
    for i in b:  # 모든 알파벳을 붙일필요없음 b에 있는것들만..
        dfs(a+i)  # 뒤에 붙이거나
        dfs(i+a)  # 앞에 붙이거나


dfs(a)
print(result)
