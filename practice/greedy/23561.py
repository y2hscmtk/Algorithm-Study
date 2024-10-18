# https://www.acmicpc.net/problem/23561
'''
3명씩 N개의 팀을 만든다.
정렬한 뒤, 앞에서부터 N개를 각 팀의 최소 값으로 배치하고
그 다음 N개를 각 팀의 중간수로 생각 -> 에너지
에너지의 최대값과 최소값을 빼서 출력

1 10 a
b 11 ? 
이런 상황에서 해당 알고리즘을 적용시키면 
b는 a보다 작은 수임이 보장되어있고, a는 11보다 큰 값임이 보장되어 있으므로 11-10이 최소값이 됨

풀이참조 : x
'''
import sys
input = sys.stdin.readline
N = int(input())
age = sorted(list(map(int,input().split()))) # 정렬하여 저장
# N번째 수부터 2N까지 수를 중간 값으로 저장
energy = age[N:N+N]
print(energy[-1] - energy[0]) # 가장 큰 에너지 - 최소 에너지