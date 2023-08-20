# https://www.acmicpc.net/problem/17390
import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
num = [0 for _ in range(N)]# 누적합을 위해 배열 생성
temp = 0
for i in range(N):
    temp += numbers[i]
    num[i] = temp
for _ in range(Q): # 쿼리 입력받기
    s,e = map(int,input().split())
    # 시작이 1이라면 해당 숫자까지의 누적합
    if s==1:
        print(num[e-1])
    elif s==e: # 시작과 끝이 같다면 해당 인덱스의 숫자
        print(numbers[s-1])
    # 그렇지 않다면 끝 숫자까지의 누적합에서 시작 숫자 이전까지의 누적합을 빼야함
    else:
        print(num[e-1]-num[s-2])
