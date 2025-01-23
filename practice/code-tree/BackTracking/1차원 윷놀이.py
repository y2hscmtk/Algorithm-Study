'''
1부터 m번까지의 번호
k개의 말 - 모두 1번 지점에 존재
말이 숫자 m번에 도착하면 1점 획득
m에 이미 도달한 말을 또 선택할 수 있지만 변화는 없다

숫자들의 집합이 순서대로 주어진다. - 숫자들을 바꿀수는 없음
-> 시도할 수 있는 모든 경우에 대해서 결과값 갱신
-> 브루트포스
'''
n,m,k = map(int,input().split())

# 이동할 칸들
numbers = list(map(int,input().split()))

# k개의 말은 초기에 모두 1번에 존재함
# 각 말에 대해서 움직일 순서를 정하고 시률레이션
max_point = 0 # 최대로 얻을 수 있는 포인트

select = [0]*(n) # n번 움직일 수 있음 -> 움직일 순서 정하기

def simulation():
    global max_point
    # 순서에 따라 시뮬레이션 수행
    curr = [1]*(k+1) # 각 말의 현재 위치
    point = 0 # 획득한 점수
    for i in range(len(numbers)):
        if curr[select[i]] < m:
            curr[select[i]] += numbers[i]
            if curr[select[i]] >= m:
                point += 1
    max_point = max(max_point, point)           
    

def select_order(idx):
    if idx == n:
        simulation()
        return

    # 1번 말부터, k말에 대해
    for i in range(1,k+1):
        select[idx] = i
        select_order(idx+1)
        select[idx] = 0

select_order(0)
print(max_point)