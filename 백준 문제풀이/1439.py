# https://www.acmicpc.net/problem/1439
'''
회진시킬 덩어리의 개수를 선택
11 00 1 0 11
위와 같을 경우 1 덩어리의 개수는 총 3개, 0 덩어리의 개수는 총 2개이므로
0 덩어리 2개를 회전시키는 것이 이득임 => 2번의 회전이 최소값이 됨

따라서 최소 각각의 그룹의 수를 카운팅하고, 그룹의 수가 더 적은 값을 정답으로 제출
'''
# 0과 1그룹의 개수
countZero,countOne = 0,0

number = input()

# 0그룹 카운팅
meetZero,meetOne = True,False # 처음만나는 1을 대비하기 위해 meetZero는 True로
for data in number:
    # 만약 1을 만났다면 => 0그룹이 끊켰음을 의미
    if data == '1' and meetZero: # 이전에 0을 만났고 1을 만난거라면 => 새로운 1그룹임
        countOne += 1
        meetZero = False # 이번에 만난건 1이므로 meetZero을 비활성화
    elif data == '0':
        meetZero = True # 0을 만났으므로 만났다는 정보를 표시

# 1그룹 카운팅
meetZero,meetOne = False,True # 처음만나는 0을 대비하기 위해 meetOne은 True로
for i,data in enumerate(number):
    # 만약 0을 만났다면 => 1그룹이 끊켰음을 의미
    if data == '0' and meetOne: # 이전에 1을 만났고 0을 만난거라면 => 새로운 0그룹임
        countZero += 1
        meetOne = False # 이번에 만난건 0이므로 meetOne을 비활성화
    elif data == '1':
        meetOne = True # 1을 만났으므로 만났다는 정보를 표시

# 두 그룹의 수를 비교하여 적은 그룹의 수를 정답으로 제출
print(countOne) if countOne < countZero else print(countZero)