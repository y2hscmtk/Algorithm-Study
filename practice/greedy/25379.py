# https://www.acmicpc.net/problem/25379
'''
인접한 두 수 끼리 위치 변경 가능
목표 : 홀수와 짝수가 인접한 경우가 최대 1번 등장하게 만들기
-> 한쪽 끝은 홀수로, 한쪽 끝은 짝수로 분리한다면 가운데만 홀수와 짝수가 인접하게 됨 
-> 즉, 홀수와 짝수가 인접한 경우가 최대 1번이 됨
=> 홀/짝 or 짝/홀 로 위치를 변경시키고 각각의 최소 횟수를 비교하여 정답으로 출력
풀이참조 : x
'''
import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int,input().split()))
result = []
evenCount,count,isRightOrder,isLeftOrder = 0,0,False,False

def right_init():
    global count,isRightOrder,isLeftOrder,evenCount
    if numbers[-1] % 2 != 0:
        evenCount = 0
        isRightOrder = True
    else:
        evenCount = 1
        isRightOrder = False
    count = 0
    
def left_init():
    global count,isRightOrder,isLeftOrder,evenCount
    if numbers[0] % 2 != 0:
        evenCount = 0
        isLeftOrder = True
    else: # 현재수가 짝수라면
        evenCount = 1
        isLeftOrder = False
    count = 0

# 1. 홀수를 오른쪽 끝으로 이동시키는 횟수 == 짝수를 왼쪽 끝으로 이동시키는 횟수
right_init()
for i in range(N-2,-1,-1):
    # 현재 수가 홀수일때, 오른쪽 수가 짝수라면
    if numbers[i] % 2 != 0 and isRightOrder == False:
        # -> 짝수 그룹의 길이만큼 위치변경 필요 => 짝수 그룹의 길이 파악 필요
        count += evenCount # 짝수 그룹의 길이만큼 스왑 반복
    elif numbers[i] % 2 == 0: # 현재수가 짝수라면
        isRightOrder = False # 오른쪽 수 홀수 아님
        evenCount += 1
result.append(count)

# 2. 홀수를 왼쪽 끝으로 이동시키는 횟수 == 짝수를 오른쪽으로 이동시키는 횟수
left_init()
for i in range(1,N):
    # 현재 수가 홀수일때 왼쪽 수가 짝수라면
    if numbers[i] % 2 != 0 and isLeftOrder == False:
        count += evenCount # 왼쪽에 존재하는 짝수 그룹의 길이만큼 스왑++
    elif numbers[i] % 2 == 0: # 현재 수가 짝수라면
        isLeftOrder = False
        evenCount += 1 # 짝수 카운트 증가
result.append(count)

print(min(result))