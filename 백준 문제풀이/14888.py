# https://www.acmicpc.net/problem/14888
'''
끼워넣을 수 있는 연산자 : +,-,*,//
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
나눗셈은 정수 나눗셈으로 몫만 취한다. 
음수를 양수로 나눌때에는 C++14의 기준을 따른다.
=> 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꾼다.
'''
import sys
input = sys.stdin.readline
N = int(input()) # 수의 개수
numbers = list(map(int,input().split()))
op = list(map(int,input().split())) # 사용 가능한 연산자의 개수
max_value, min_value = -sys.maxsize, sys.maxsize
# 수의 위치는 고정, 달라지는건 연산자
# 만들 수 있는 모든 연산의 경우의 수 만들고 그에 따른 결과 업데이트
selected = []
def dfs(depth):
    global selected,max_value,min_value
    if depth == N-1: # 연산자는 최대 N-1개만큼 뽑을 수 있음
        # 다 뽑았으면 연산 수행후 업데이트
        max_value = max(max_value,calc())
        min_value = min(min_value,calc())
        return
    for i in range(len(op)):
        if op[i] != 0: # 사용 가능하다면
            selected.append(i)
            op[i]-=1
            dfs(depth+1)
            # 백트래킹
            selected.pop()
            op[i]+=1

def calc():
    # numbers를 대상으로 앞에서부터 연산자에 맞춰서 연산 수행
    temp = numbers[0]
    for i in range(1,N):
        if selected[i-1] == 0: # 0번은 +
            temp += numbers[i]
        elif selected[i-1] == 1: # 1번은 -
            temp -= numbers[i]
        elif selected[i-1] == 2: # 2번은 *
            temp *= numbers[i]
        else: # 3번은 나누기
            # 양수로 바꾼뒤 몫을 취하고 그 몫을 음수로 바꾼다.
            if temp < 0 or numbers[i] < 0:
                temp = abs(temp); numbers[i] = abs(numbers[i])
                temp//=numbers[i]
                temp = -temp
            else:
                temp//=numbers[i]
    return temp

dfs(0)
print(max_value)
print(min_value)
