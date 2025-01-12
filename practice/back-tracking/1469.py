# https://www.acmicpc.net/problem/1469
'''
조건
1. X에 들어있는 모든 수는 숌 사이 수열 S에 정확히 두 번 등장해야 한다.
2. X에 등장하는 수가 i라면, S에서 두 번 등장하는 i사이에는 수가 i개 등장해야 한다.

길이 2N의 수열 생성
'''
N = int(input())
numbers = sorted(list(map(int,input().split())))

# X의 원소는 0보다 크거나 같고 16보다 작거나 같은 정수이다.
count = [0]*(17) # 각 숫자를 몇번 사용했는지 확인

# 원하는 숫자를 해당 위치에 넣는것이 확인한지 중간중간 확인
def is_possible(idx,num):
    # 먼저 num이 어디 인덱스에 최초로 위치하는지 확인
    first_idx = float('inf')
    for i in range(idx):
        if select[i] == num:
            first_idx = i
            break
    # 아직 해당 수를 넣지 않았다면 -> 무조건 넣을 수 있음
    if first_idx == float('inf'):
        return True
    if idx-first_idx-1 == num: 
        return True
    return False
   

select = [0]*(2*N) # 선택한 숫자들 저장 용도
# 2N개의 숫자 선택
# 같은수가 최대 2번까지만 선택 가능함
def select_num(idx):
    global find
    if find == True: # 찾은 경우는 더이상 탐색할 필요가 없다
        return
    if idx == 2*N: # 2N개 선택시 -> 조건을 만족하는지 확인
        print(*select)
        find = True
        return
    # numbers에 있는 숫자들 최대 2개까지 선택 가능
    for i in range(len(numbers)):
        num = numbers[i]
        # 아직 2개 선택하지 않은 경우이고, 목표한 수를 해당 위치에 넣을 수 있는 상황이라면
        if count[num] < 2 and is_possible(idx,num):
            count[num] += 1
            select[idx] = num
            select_num(idx+1)
            select[idx] = 0 # 백트래킹
            count[num] -= 1

find = False
select_num(0)
if not find: # 가능하지 않은 경우
    print(-1)