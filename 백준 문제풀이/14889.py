# https://www.acmicpc.net/problem/14889

'''
사람은 총 N명(짝수)이고 N/2명씩 두 팀으로 나눈다.
팀으로 나눌때 능력치는 다음과 같이 정한다.
N=4이고, S가 아래와 같은 경우를 살펴보자.

i\j	1	2	3	4
1	 	1	2	3
2	4	 	5	6
3	7	1	 	2
4	3	4	5	 
예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

스타트 팀: S12 + S21 = 1 + 4 = 5
링크 팀: S34 + S43 = 2 + 5 = 7
1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10

두 팀의 능력치 차이의 최솟값을 구하라
'''
import sys
from itertools import combinations

n = int(input())  # 인원수

member = [i for i in range(1, n+1)]  # 멤버 표시
member = set(member)

synergy = [list(map(int, input().split())) for _ in range(n)]  # 시너지 입력받기

# Sij는 i행 j열과 j행 i열의 합과 같다.

# 계산할수 있는 모든 경우의 수를 조합으로 구하고, 2중 반복문으로 나눠진 배열에서 각각 시너지 합을 구한뒤,
# 두 차가 최소가 되도록 업데이트한다.

# 두 팀의 능력치 차를 저장할 변수(정답)
result = sys.maxsize

# 팀을 절반으로 나누기 위해 절반을 뽑고, 기존 배열에서 해당 수들을 제외한 값들로 새로운 배열을 만든다.
for array in combinations(member, n//2):
    # 두 팀 만들기
    team_start = array
    team_link = member-set(array)

    # 만들어진 두 팀에 대해서 각각의 시너지 구하기
    team_start_stats = 0
    team_link_stats = 0

    # 스타트팀의 능력치 합 구하기
    for i, j in combinations(team_start, 2):
        team_start_stats += (synergy[i-1][j-1] + synergy[j-1][i-1])
    # 링크팀의 능력치 합 구하기
    for i, j in combinations(team_link, 2):
        team_link_stats += (synergy[i-1][j-1] + synergy[j-1][i-1])

    # 두 팀의 능력치 차 갱신
    result = min(result, abs(team_start_stats-team_link_stats))
print(result)
