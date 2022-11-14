# https://www.acmicpc.net/problem/2751

# 선택 정렬 방식으로 풀어보기

n = int(input())

list = []
for _ in range(n):
    list.append(int(input()))

# 여기서부터 정렬 시작
# 오름차순으로 정렬시키는것이 목표
# 선택 정렬 => swap을 이용해서 오른쪽 리스트의 가장 큰값과 인덱스 교환
for i in range(n):
    large = i  # 0번째 부터 비교
    for j in range(i+1, n, 1):  # 1번째 인덱스부터 마지막 인덱스까지 중
        if list[j] > list[large]:  #
            large = j  # 가장 큰 값의 인덱스 업데이트
        list[j], list[large] = list[large], list[j]


for i in list:
    print(i)
