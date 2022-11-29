# https://www.acmicpc.net/problem/1764

'''
듣도 못한 사람의 그룹과 보도 못한 사람의 그룹
두 그룹에 모두 속하는 듣보잡의 수를 구하고 듣보잡을 사전순으로 출력할것
'''

'''
아이디어 : 모두 입력받아 저장한 후, 하나의 배열에서 하나에 속한것들을 새로운 배열에 저장한다.
이후 배열을 정렬하고 출력한다 => 시간초과 실패

아이디어2 : 집합 자료형을 사용하여 데이터를 입력받고, 교집합 메소드를 이용하여 분류한다. 
이후 배열로 변환하여 정렬한후 하나씩 출력한다.
'''

n, m = map(int, input().split())

a = set()  # 집합 자료형 사용 => 중복허용x, 고유한 키값,순서 없음, 중괄호 등을 이용해서 표현가능, add()로 더함
b = set()


# 데이터 입력받기
for _ in range(n):
    a.add(input())  # 듣잡에 삽입
for _ in range(m):
    b.add(input())  # 보잡에 삽입

ab = list(a.intersection(b))  # 둘의 교집합을 ab로 만듬 => 집합의 형태이므로 정렬을 하기 위해 배열로 변경

ab.sort()  # 사전순으로 정렬

# 탐색 시작
# for item in a:
#     if item in b:  # b에 속해있다면
#         ab.append(item)  # 듣보잡에 삽입

# ab.sort()  # 사전순으로 정렬한 후에
print(len(ab))
for data in ab:
    print(data)  # 하나씩 출력한다.
