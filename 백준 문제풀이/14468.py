# https://www.acmicpc.net/problem/14468
'''
각 알파벳의 시작과 끝 좌표 딕셔너리로 기록
A~Z까지
B~Z까지
C~Z까지
...
돌면서 경로 겹치는 쌍의 개수 증가
'''
data = list(input())
dict = {}
for i, alpha in enumerate(data):
    if alpha not in dict:  # dict에 없다면 시작 좌표 배열로 기록
        dict[alpha] = [i]
    else:  # 이미 dict에 있다면 끝좌표 기록
        dict[alpha].append(i)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
'''
A~Z까지
B~Z까지
C~Z까지 .. 경로가 겹치는 알파벳 파악
'''
result = 0  # 경로가 겹치는 쌍의 개수
for i in range(len(alphabet)):
    a_start, a_end = dict[alphabet[i]]
    for j in range(i, len(alphabet)):
        b_start, b_end = dict[alphabet[j]]
        # a가 s와 e 사이에 존재하고, b가 e밖에 존재한다면 경로가 겹치는것임
        if a_start < b_start < a_end and a_end < b_end:
            result += 1  # [A,B]로 정답 쌍 증가
        elif b_start < a_start < b_end and b_end < a_end:
            result += 1
        '''
        # A가 B보다 먼저 지나간다는 보장이 없음
        '''
print(result)
