# https://www.acmicpc.net/problem/10816

'''
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
'''
n_length = int(input())
n = list(map(int, input().split()))
n.sort()  # 이진탐색을 위해 정렬
m_length = int(input())
m = list(map(int, input().split()))

# 참고한 사이트
# https://soooprmx.com/bisect-%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EB%93%AC/
# https://hongcoding.tistory.com/12


# 파이썬 라이브러리 bisect를 문제상황에 맞도록 구현
# 일치하는 데이터가 많을 경우, 가장 왼쪽 인덱스를 리턴함
def bisect_left(card):
    start, end = 0, n_length
    while start < end:
        mid = (start+end)//2
        if n[mid] < card:  # card가 오른쪽 영역에 존재하면
            start = mid + 1  # 탐색 시작범위를 mid 이후로
        else:  # 왼쪽영역에 카드가 존재하거나, mid위치에 카드가 존재한다면
            end = mid  # 탐색 끝범위를 mid까지로
    # start == end면 탐색성공, start>end면 탐색 실패
    return start


# 일치하는 데이터가 많을 경우, 가장 오른쪽 인덱스를 리턴함
def bisect_right(card):
    start, end = 0, n_length
    while start < end:
        mid = (start+end)//2
        if n[mid] > card:  # card가 리스트 왼쪽 영역에 존재하면
            end = mid  # 탐색 끝범위를
        else:  # 오른쪽 영역에 card가 존재하거나, mid위치에 card가 존재한다면
            start = mid+1  # 탐색 시작 범위를 mid부터로
    # start == end면 탐색성공, start>end면 탐색 실패
    return start


# 이분 탐색을 진행하다 원하는 데이터를 찾으면 해당 인덱스를 기준으로 앞뒤로 카운팅하여 출력(같은 숫자의 경우 앞뒤에 배치되어 있을것)
# 결과 출력
for card in m:
    left_index = bisect_left(card)
    right_index = bisect_right(card)
    print(right_index-left_index, end=' ')
