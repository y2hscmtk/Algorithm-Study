# https://www.acmicpc.net/problem/1253
'''
아이디어1
1. 정렬
2. 가장 오른쪽 수부터 판단
3. 정렬이 된 시점에서, 가장 오른쪽 수의 왼쪽 수들은 해당 수 보다 작음
4. 따라서 왼쪽 수들에 대해서 양 끝수를 더해가며 비교하면 되지않을까(투 포인터)
=> 수정 : 모두 같은 수일 경우, 즉 0 0 0 인경우 답이 3개가 됨
=> 따라서 모든 구간에 대해 검색해야할듯(자기 숫자 제외)
'''
import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
# 정렬
numbers.sort()
result = 0 # 좋은 수의 개수
# 가장 오른쪽 수 부터 타켓으로 삼고, 한칸씩 왼쪽으로 이동하며 해당 수에 대해 '좋은 수'인지 확인
for i in range(n-1,-1,-1):
    target = numbers[i]
    start,end = 0,n-1 # 가장 오른쪽 값을 탐색 대상으로
    # start 혹은 end가 target과 같은 index라면 범위 한칸씩 줄이기
    if start==i:
        start+=1
    if end==i:
        end-=1
    
    # 이분 탐색 수행
    while start<end:
        # 더해서 해당 수가 되는 경우를 발견했다면
        if numbers[start] + numbers[end] == target:
            result += 1 # 좋은수 카운트
            break # 무한반복 탈출
        # target보다 크다면
        elif numbers[start] + numbers[end] > target:
            end-=1 # 한칸 아래로 당김
            # 당긴 결과가 target과 같은 인덱스라면 더 당김
            if end==i:
                end-=1
        else: # target보다 작다면
            start+=1 # 한칸 위로 당김
            # 당긴 결과가 target과 같은 인덱스라면 더 당김
            if start==i:
                start+=1
print(result)