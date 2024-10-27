# https://www.acmicpc.net/problem/11509
'''
풀이참조
'화살의 개수' 를 최소화 하는 것이 목표, 화살이 존재한다면 풍선은 반드시 터짐
-> 모든 위치에 대한 화살의 개수를 배열을 통해 관리
-> 최종적으로 존재하는 화살의 개수가 사용한 화살의 수가 됨(화살의 높이가 변할뿐 사라지지 않으므로) 
'''
import sys
input = sys.stdin.readline

N = int(input())
balloons = list(map(int,input().split()))
# i번째 높이에 존재하는 화살의 위치 기록
arrows = [0]*(1000000+1) # 풍선은 최대 1000000 높이에 존재 가능

# 풍선이 존재하는 각 위치에 대해서
for height in balloons:
    if arrows[height] > 0: # 해당 위치에 화살이 존재한다면
        arrows[height] -= 1 # 풍선을 터뜨렸으므로, 화살의 높이는 -1이 된다.
        arrows[height-1] += 1 # height 높이에 존재했던 화살이 height-1의 위치로 이동하였으므로 +1
    else: # 아직 해당 위치에 화살이 존재하지 않을 경우
        # height 높이에 화살을 하나 발사시켜 풍선을 제거한다. -> 화살은 최종적으로 height - 1의 위치에 도달하게 된다.
        arrows[height-1] += 1 


# 최종적으로 남아있는 화살의 개수가 곧 사용한 화살의 개수
print(sum(arrows))