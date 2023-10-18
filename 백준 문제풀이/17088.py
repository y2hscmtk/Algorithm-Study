# https://www.acmicpc.net/problem/17088
'''
브루트포스
각 숫자에 대해 한번씩 연산을 적용시킨후 등차수열을 만족하는지 확인
숫자를 하나만 바꿔야 될 수도 있고, 안바꿔도 될수도 있음
'''
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))

# 해당 수열이 등차수열을 만족하는지 확인
def check():
    diff = data[1]-data[0]
    for i in range(2,len(data)):
        temp = data[i] - data[i-1]
        if temp != diff:
            return False
    return True # 문제없이 통과했다면 등차수열임