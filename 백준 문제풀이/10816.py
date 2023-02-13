# https://www.acmicpc.net/problem/10816

'''
N개의 정수 들중에 X라는 정수가 존재하는지 맞추기

n개의 자연수가 주어지고, m개의 자연수들이 주어진다. 
n개의 자연수로 이루어진 배열에 m개의 자연수가 존재하는지 탐색한다.

M(1 ≤ M ≤ 100,000)
'''

'''
아이디어1 : 배열을 입력받고, 배열을 오름차순으로 정렬시킨후, 이진탐색을 통해 m개의 자연수들을 탐색하면 될듯하다.
'''

n = int(input())
array = list(map(int, input().split()))  # 배열의 형태로 공백으로 분리하여 자연수를 입력받기

array.sort()  # 이진탐색을 위해 배열 오름차순 정렬

m = int(input())
num = list(map(int, input().split()))  # 탐색에 대입하기 위한 숫자 배열


# 이진탐색 함수 정의
def binary_search(list, start, end, n):  # 배열, 시작노드, 끝노드
    while start <= end:  # 다음 조건을 만족하는동안 탐색
        middle = (int)((start+end)/2)  # 중간값 파악
        if n < list[middle]:  # 탐색하고자 하는 값이 중간값보다 작다면
            end = middle - 1  # 끝점의 범위를 좁혀서 왼쪽에서 탐색
        elif n > list[middle]:  # 탐색하고자 하는 값이 중간값보다 크다면
            start = middle + 1  # 시작점의 범위를 앞으로 당겨서 오른쪽에서 탐색
        else:  # 원하는 값을 찾았을때
            return True  # 탐색이 성공했음을 리턴함
    return False  # 탐색이 실패했음을 알림(리턴없이 반복문에서 탈출)


# 결과 출력
for key in num:
    if binary_search(array, 0, n-1, key):
        print(1)  # 탐색 성공시 1
    else:
        print(0)  # 실패시 1
