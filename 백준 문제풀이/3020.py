# https://www.acmicpc.net/problem/3020
'''
아이디어 : 이분탐색
최소로 장애물을 부딪히는 횟수를 알아야 하므로, 높이를 1씩 높이면서(1~H+1) 이분탐색 반복 수행

석순의 부딛히는 횟수 처리 => 홀수번에 입력받은 값을 석순 배열에 삽입후 정렬
1,3,5,7,3,3,4,2 가정시 => 1,2,3,3,3,4,5,7 => 같은 값이 여러번 등장할수 있고 우리가 알고 싶은것은 장애물이 부딛히는 횟수
개똥벌레가 탐색하는 위치가 3이라고 가정시, 3이랑 크거나 같은 값 모두 충돌 인덱스를 기준으로 LOW와 HIGH를 설정, low=0, high=7, middle = 3이됨
3번째 인덱스의 값은 조건을 만족하므로, 그보다 낮은 인덱스에서 조건을 만족하는지 확인 low=0,high=3, => middle=1, 1번째 인덱스는 조건 만족x 
low=1,high=3, middle=2, 2에서 조건을 만족 => 인덱스 2번 이후의 값에서 모두 충돌하게 된다. => 동일한 값이 존재한다면 가장 왼쪽값에서 찾아야한다.

종순이 부딛히는 횟수 처리 => 짝수번에 입력받은 값을 H-value 형식으로 종순 배열에 삽입후 정렬
3,4,5,1,2 이라고 가정하고 H = 5일때 => [2,1,0,4,3]이 저장됨 => 정렬시 [0,1,2,3,4]
개똥벌레가 탐색하는 위치가 3번이라고 가정할때 3보다 작은 값에 대해서 모두 부딛힌다.(빼준것이므로) 
=> value값 3을 찾기 위해 이분탐색을 수행한다 => 가장 오른쪽에 있는 3을 찾아야한다. 

석순과 종순에 대해서 카운트 수행하고, 최소값을 업데이트한다. 각 카운팅 횟수에 대해 사전에 배열에 기록해두고 최소값과 같은 값의 수를 출력한다.
'''
import sys
from bisect import bisect_left,bisect_right # 이분탐색을 도와주는 라이브러리
N,H = map(int,input().split()) # N개의 장애물이 존재(짝수인덱스는 석순, 홀수 인덱스는 종유석), H는 높이

stalagmite = [] # 석순
stalactite = [] # 종유석

for i in range(N):
    size = int(input())
    if i%2==0: # 석순이면 석순 배열에
        stalagmite.append(size)
    else: # 종유석이면 종유석 배열에 H-value로 삽입
        stalactite.append(H-size)
        
# 입력이 끝나면 각 배열 정렬
stalagmite.sort() # 오름차순 정렬
stalactite.sort() # 오름차순 정렬

# 각 배열의 크기
stalagmite_size = len(stalagmite)
stalactite_size = len(stalactite)

min_count = sys.maxsize # 최소 횟수
# 층별로 부딛히는 횟수를 저장하기 위한 배열
crash_count = []

# 높이 1부터 높이 H까지 각 배열에 대해서 이분탐색 수행
for i in range(1,H+1):
    count = 0 # 장애물과 부딛히는 횟수 초기화
    
    # 석순과 부딛히는 횟수(i와 크거나 같을때)
    index = bisect_left(stalagmite,i) # 해당 값과 동일한 값들 중, 가장 왼쪽 인덱스
    count += stalagmite_size-index # 전체 석순 개수에서 빼주면 몇개 충돌하는지 알 수 있음
    
    # 종유석 충돌 계산
    index = bisect_right(stalactite,i-1) # 오른쪽 값 반환
    count += index # index가 충돌 횟수가 됨
    
    crash_count.append(count) # 부딛힌 횟수 기록
    min_count = min(min_count,count) # 최소 횟수 업데이트
    
print(min_count,end=' ')
# 최소횟수인 값의 수 출력
print(crash_count.count(min_count))