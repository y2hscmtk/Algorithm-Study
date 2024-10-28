# https://www.acmicpc.net/problem/20115
'''
에너지드링크를 다른 병으로 이동하는 과정에서 절반의 손실이 발생
-> 적은 양의 에너지드링크를 이동시키는 것이 최소한의 손실을 발생시킴
-> 정렬 후 앞에서부터 가장 마지막 에너지드링크(최대 용량)으로 이동 반복
풀이참조 : x
'''
import sys
input = sys.stdin.readline
N = int(input())
drink = sorted(list(map(int,input().split())))
result = drink[-1] # 마지막 음료수
for i in range(N-1):
    result += (drink[i] / 2)
print(result)