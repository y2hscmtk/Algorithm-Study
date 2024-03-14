# https://www.acmicpc.net/problem/1806
'''
투 포인터 활용
left,right를 모두 0으로 두고 시작
left에서부터 right까지의 합이 m을 넘지 못한다면 right 오른쪽으로 한 칸 이동
m을 넘었다면 가장 짧아지게 만드는 것이 목표이므로 left 한칸 이동하고 값 줄이기
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
numbers = list(map(int,input().split()))
left,right = 0,0
result = sys.maxsize # 가장 짧은 길이
temp = 0 # left~right까지의 합
while True:
    if temp >= m: # 합이 m이상이라면
        result = min(result,right-left) # 현재까지의 길이 갱신
        # left를 줄여서 어디까지 길이를 줄일 수 있는지 확인
        temp -= numbers[left]
        left+=1
    elif right == n: # 끝까지 탐색했다면 종료
        break
    else: # m 미만이라면 right 오른쪽으로 이동
        temp += numbers[right] # 오른쪽 값 더하기
        right+=1
# 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
print(result if result!=sys.maxsize else 0)