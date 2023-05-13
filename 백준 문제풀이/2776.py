# https://www.acmicpc.net/problem/2776

'''
첫째 줄에 테스트케이스의 개수 T가 들어온다. 
다음 줄에는 ‘수첩 1’에 적어 놓은 정수의 개수 N(1 ≤ N ≤ 1,000,000)이 입력으로 들어온다. 
그 다음 줄에  ‘수첩 1’에 적혀 있는 정수들이 N개 들어온다. 그 다음 줄에는 ‘수첩 2’에 적어 놓은 정수의 개수 M(1 ≤ M ≤ 1,000,000) 이 주어지고, 
다음 줄에 ‘수첩 2’에 적어 놓은 정수들이 입력으로 M개 들어온다. 
모든 정수들의 범위는 int 로 한다.
각각의 수에 대하여, ‘수첩1’에 있으면 1을, 없으면 0을 출력하는 프로그램을 작성해보자.
'''


# 이분탐색 정의
def check(num):
    low,high = 0,n # 인덱스 0부터 인덱스 n까지..
    while low<high:
        mid = (low+high)//2 # 중간 인덱스
        # mid번째 인덱스의 값과 num비교
        # 일치한다면
        if data1[mid] == num:
            return 1
        elif data1[mid] < num: # 더 작다면
            low = mid+1 # 오른쪽에서 탐색하기
        elif data1[mid] > num: # 더 크다면
            high = mid # 왼쪽에서 탐색하기
    # 탐색 결과 원하는 숫자를 찾지 못했다면
    return 0


for _ in range(int(input())): # t번만큼 반복
    n = int(input())
    # 수첩 1에 n개만큼 데이터 입력받기
    data1 = list(map(int,input().split()))
    m = int(input())
    # 수첩 2에 m개만큼 데이터 입력받기
    data2 = list(map(int,input().split()))

    data1.sort() # 이분탐색을 위해 오름차순 정렬
    # 수첩2의 수들이 수첩1에 있으면 1을, 없으면 0을 출력한다.
    for num in data2:
        print(check(num)) # num이 data1에 있으면 1, 없으면 0
        