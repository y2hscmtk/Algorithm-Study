# 이진 탐색 문제

# 동빈이네 매장에는 N개의 부품이 있다. 각 부품은 일련번호를 갖고 있다.
# 손님이 M개 종류의 부품을 찾을 때, 동빈이는 해당 부품의 일련번호를 확인하여 매장에 있는지 확인한다.

# 입력 조건
# 첫째 줄에 정수 N이 주어진다.
# 둘째 줄에 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1000000이하이다.
# 셋째 줄에는 정수 M이 주어진다.
# 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.
# 출력 조건
# 첫째 줄ㄹ에 공백을 ㅗ구분하여 각 부품이 존재하면 yes를 없으면 no를 출력한다.

n = int(input())
array_n = list(map(int, input().split()))

m = int(input())
array_m = list(map(int, input().split()))

# 이진 탐색을 활용하여 문제를 해결한다.
array_n.sort()

# 이진 탐색의 원리는 다음과 같다.
# 1 2 3 4 5 6 7 8 9 10 다음과 같이 숫자가 주어질때,
# 각각의 인덱스는 0 ~ 9가 된다. 이때 start = 0, end = 9, mid = 0+9//2 라고 하자
# mid와 찾고자 하는 수를 비교하여해당 수가 mid보다 작다면 end의 값을 mid-1로 하여 재탐색하고
# 찾고자 하는 수가 mid보다 크다면, start = mid+1로 하여 재탐색한다.
# 데이터를 점점 반으로 줄여나가서 찾고자 하는 수가 있다면 반환하고, 탐색에 실패한다면 없는것이다.


def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:  # target이 배열의 왼쪽 부분에 존재한다면
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


for i in array_m:
    if binary_search(array_n, i, 0, n-1) == True:
        print("yes", end=' ')
    else:
        print("no", end=' ')