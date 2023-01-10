# https://www.acmicpc.net/problem/10815

'''
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 

둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 

숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 

넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며,

이 수는 공백으로 구분되어져 있다. 

이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

'''

# 카드의 개수 입력받기
n = int(input())

# 카드 리스트 입력받기
card_list = list(map(int, input().split()))

# 탐색할 카드의 개수 입력받기
m = int(input())

# 탐색할 카드 리스트 입력받기
search_list = list(map(int, input().split()))

# 이분 탐색을 이용하기 위해 카드리스트를 정렬한다.
card_list.sort()

for i in range(len(search_list)):
    # 탐색할 가드 선정
    card = search_list[i]

    # 이분탐색 시작
    start = 0  # 시작 인덱스
    end = len(card_list)  # 마지막 인덱스

    for j in range(start, end):

        # 탐색 종료 조건 설정
        if start >= end:
            # 탐색 실패
            search_list[i] = 0
            break

        # 가운데 인덱스 선택
        middle = (start+end)//2

        # 가운데 값이 탐색카드와 같을때 => 탐색종료
        if card == card_list[middle]:
            # 탐색 성공
            search_list[i] = 1
            break
        # 가운데 카드보다 탐색카드가 클때
        elif card > card_list[middle]:
            # 탐색 범위 수정
            start = middle+1

        # 가운데 카드보다 탐색카드가 작을때
        elif card < card_list[middle]:
            end = middle


# 탐색 결과 출력
for card in search_list:
    print(card, end=" ")
