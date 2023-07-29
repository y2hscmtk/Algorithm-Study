# https://www.acmicpc.net/problem/2343
'''
구하고 싶은 값 : 블루레이의 크기 중 최소값
=> 블루레이의 크기를 구하고자 하는 값으로 설정해야함
start = 0, end = sys.maxsize
블루레이의 크기 => 한 블루레이에 속한 강의 크기의 합
'''
import sys
start,end = 0,sys.maxsize
n,m = map(int,input().split())
videos = list(map(int,input().split()))
max_video = max(videos)
result = sys.maxsize
'''
블루레이의 크기를 임시로 설정
해당 블루레이의 크기로 모든 블루레이를 저장할때, 몇개의 블루레이가 나오는지 확인
블루레이의 개수가 m개에 못미친다 => 블루레이의 크기가 너무 크다(너무 크게 쪼갰다)
=> 왼쪽 영역(블루레이의 크기가 작아지는 영역)으로 탐색 좁히기
블루레이의 개수가 m개를 초과한다 => 블루레이의 크기가 너무 작다(너무 잘게 쪼갰다)
=> 오른쪽 영역(블루레이의 크기가 커지는 영역)으로 탐색 좁히기
'''
while start<end:
    mid = (start+end)//2 #한 블루레이의 크기 설정
    # 설정한 크기로 모든 영상을 하나이상 넣을 수있는지 확인
    if mid<max_video:
        # 가장 큰 영상의 크기보다 블루레이의 크기가 작다면
        start=mid+1 # 오른쪽 영역에서 탐색해야함
        continue

    count, temp = 1,0 # 총 몇개의 블루레이가 만들어지는지, 현재 블루레이에 얼만큼 담았는지
    # 앞에서부터, 블루레이에 담을 수 있는 만큼, 최대한 담는다.
    for i in range(len(videos)):
        # 현재 블루레이에 해당 영상을 담았을때, 설정해둔 블루레이의 크기를 초과하는지 확인
        if temp + videos[i] <= mid: # 초과하지 않는다면
            temp += videos[i] # 영상 담기
        else: # 초과한다면
            count+=1 # 현재 블루레이에 담을 수 있는 만큼 담았음
            temp = videos[i] # 다음 블루레이에 영상 넣기(새롭게 시작)
    
    # mid로 블루레이의 크기를 설정했을때, 몇개의 블루레이가 생성됐는지 확인
    if count<=m: # 만들고 싶은 블루레이 양만큼 담지 못했다면, 혹은 원하는 만큼 생성됐다면
        # 더 작은 크기의 블루레이에서 m개의 블루레이가 생성되는지 확인해야함
        end = mid
        result = min(result,mid) # 기존 최소값과 현재 측정된 크기중 최소값 삽입
    else: # count>m => 블루레이의 크기를 너무 작게 설정했음을 의미함(너무 잘게 쪼개졌음)
        start = mid + 1 # 블루레이의 크기를 크게 설정하여 다시 탐색

print(result)
