# https://www.acmicpc.net/problem/21758
'''
음수가 없으므로, 최대한 많은 값을 얻는 것이 이득
그리디, 누적합
<풀이참조>
1. 벌 벌 꿀 : 벌(고정) 벌(변수) 꿀(고정)
2. 꿀 벌 벌 : 꿀(고정) 벌(변수) 벌(고정)
3. 벌 꿀 별 : 별(고정) 꿀(변수) 별(고정)

=> 경우의 수 펼치기(모든 경우 생각)
'''
import sys
input = sys.stdin.readline

N = int(input())
honey = list(map(int,input().split()))
result = 0
prefix = [h for h in honey]
for i in range(1,N):
    prefix[i] += prefix[i-1]

# 1. 꿀 벌 벌
for i in range(1,N-1):
    # 오른쪽 끝 벌이 섭취하는 꿀 : prefix[N-2] - honey[i] ; 두번째 벌이 i번째 위치할 시, 섭취 불가, 현재칸 섭취 불가(N-1-1)
    # 두번째 벌이 섭취하는 꿀 : prefix[i-1] ; 현재칸은 섭취 불가능하므로
    result = max(result, prefix[N-2]-honey[i]+prefix[i-1])

# 2. 벌 벌 꿀
for i in range(1,N-1):
    # 왼쪽 끝 벌이 섭취하는 꿀 : pefix[N-1] - honey[0] - honey[i] 
    # -> 왼쪽 끝 값을 제외한 모든 칸 섭취 가능, 두번째 벌 위치(honey[i]) 섭취 불가
    # 두번째 벌이 섭취하는 꿀 : prefix[N-1] - prefix[i] ; 전체 합에서 현재칸까지의 누적합은 섭취 불가능(이후 부터 섭취 가능)
    result = max(result, prefix[N-1]-honey[0]-honey[i] + prefix[N-1]-prefix[i])

# 3. 벌 꿀 벌
for i in range(1,N-1):
    # 양쪽 끝 벌이 섭취하는 꿀의 양 : prefix[-1]-honey[0]-honey[-1]
    # 꿀이 위치한 칸은 양쪽 끝 벌이 둘다 섭취 가능 : honey[i]
    result = max(result, prefix[-1]-honey[0]-honey[-1]+honey[i]) # 0,-1번째 꿀은 합계에서 제외(벌)
    
print(result)