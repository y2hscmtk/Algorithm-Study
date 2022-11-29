# https://www.acmicpc.net/problem/1764

'''
듣도 못한 사람의 그룹과 보도 못한 사람의 그룹
두 그룹에 모두 속하는 듣보잡의 수를 구하고 듣보잡을 사전순으로 출력할것
'''

'''
아이디어 : 모두 입력받아 저장한 후, 하나의 배열에서 하나에 속한것들을 새로운 배열에 저장한다.
이후 배열을 정렬하고 출력한다
'''

n, m = map(int, input().split())

a = []  # 듣도 못한 사람
b = []  # 보도 못한 사람
ab = []  # 듣도 보도 못한 사람

for _ in range(n):
    a.append(input())
for _ in range(m):
    b.append(input())

# 탐색 시작
for item in a:
    if item in b:  # b에 속해있다면
        ab.append(item)  # 듣보잡에 삽입

ab.sort()  # 사전순으로 정렬한 후에
print(len(ab))
for data in ab:
    print(data) # 하나씩 출력한다.
