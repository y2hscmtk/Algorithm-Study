# https://www.acmicpc.net/problem/7795
t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()
    # a배열의 각 숫자에 대해서 카운팅 작업 시행
    count = 0
    
    # mid보다 많은 것의 개수를 반환한다
    # 이분탐색
    for i in range(len(a)):
        check = a[i] # 현재 비교할 숫자 설정
        # b의 모든 인덱스와 비교하여
        # b의 특정 수 중에서 
        # check보다 커지도록 하는 최소 단위 설정
        low,high = 0,m
        # 가장 작은 값과 비교하여 더 작다면 => 이분탐색 시행x
        if check<=b[0]:
            continue
        elif check>b[-1]: # 가장 큰 값보다도 크다면 시행 필요x
            count += m
        else:
            while low<high:
                mid =(low+high)//2
                if b[mid] < check:
                    low = mid+1
                else:
                    high = mid
                    index = high
                    
            count += index
    print(count)
