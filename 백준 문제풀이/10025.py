# https://www.acmicpc.net/problem/10025

n,k = map(int,input().split())

max_index = -1

ice = [0]*1000001 # 얼음의 누적합 기록용 배열

for i in range(n):
    g, x = list(map(int,input().split()))
    ice[x] = g # x위치에 g만큼 얼음이 있다.
    max_index = max(max_index,x) # 최대 좌표를 알기 위해


# 윈도우 크기 설정
size = 2*k + 1 # 좌우로 k만큼, 그리고 해당인덱스+1

# 윈도우 범위 내의 초기 합
window = sum(ice[:size]) 

result = window # 최대로 가져갈수있는 얼음의 양

for i in range(size,max_index+1):
    # 다음 인덱스의 값을 더하고, 기존 값의 가장 첫 인덱스를 뺀다.
    # size가 유지된다~
    window += (ice[i]-ice[i-size]) # 창문을 한칸씩 민다고 생각 => 새로운 창을 추가하고, 가장 앞의 창을 제거
    result = max(result,window)
    
print(result)