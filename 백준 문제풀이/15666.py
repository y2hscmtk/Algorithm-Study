# https://www.acmicpc.net/problem/15666
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split())))

def dfs(curr,start):
    global result
    if len(curr) == m: # m개의 수를 뽑았다면
        print(*curr)
        return
    used = [False]*(max(numbers)+1) # 해당 수를 사용했는지 사용하지 않았는지
    for i in range(start,n):
        num = numbers[i]
        if not used[num]:
            used[num] = True # 사용처리
            curr.append(num) # 수 사용 처리
            dfs(curr,i)
            curr.pop() # 백트래킹
dfs([],0)