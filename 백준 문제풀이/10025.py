# https://www.acmicpc.net/problem/10025

'''
최초 데이터를 입력받을때,
정렬을 하여 누적합의 형식으로 배열에 저장

현재 앨버트가 자리를 잡은 위치(i)에서
-k~ +k 범위안의 모든 얼음의 최대값
=> data[i+k] - data[i-k]  만큼의 얼음을 가져갈수 있을것

앨버트의 위치는 0<x<1000000사이 => 이분탐색?
'''
n,k = map(int,input().split())

max_index = -1
result = 0 # 가져갈수 있는 얼음의 최대값 
data = []

for i in range(n):
    g, x = list(map(int,input().split()))
    max_index = max(max_index,x) # 최대 좌표를 알기 위해
    data.append([x,g]) # x좌표에 g만큼의 얼음이 있다.
data.sort() # 좌표를 기준으로 오름차순 정렬

ice = [0]*(max_index+k+1) # 얼음의 누적합 기록용 배열

for x,g in data:
    # x보다 높은 인덱스에 g저장
    for i in range(x,len(ice)):
        ice[i] += g # 얼음 누적 기록


# 가져갈수 있는 얼음의 양이 갱신되는지 확인 => 갱신된다면 True리턴
def check(m):
    temp = ice[m+k] - ice[m-k] # 가져갈수 있는 얼음의 양 기록
    if temp>result: #더 많이 가져갈수 있다면
        result = temp # result값 갱신
        return True
    else:
        return False


# 가져갈수있는 얼음의 양이 최대값이 될때까지 이분탐색
# 적정 좌표 탐색
low,high = 1, max_index # max_index로부터 오른쪽으로 k만큼 떨어진 곳까지 탐색이 가능하므로
while low<high:
    mid =(low+high)//2
    