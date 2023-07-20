# https://www.acmicpc.net/problem/17281
'''
입력 데이터로 각 이닝에서의 결과가 주어진다.
우리 팀의 최고 득점 타순을 구하는 것이 목표이므로, 상대팀의 정보는 신경 쓸 필요없음
아웃 이후, 바로 다음 이닝으로 넘어간다.
=> 결국 우리가 해줘야 할 일은 1번 타자를 4번에 고정시킨 상태로 나머지 순서를 정해서 배열을 넘겨주는 것
정해놓은 배열의 순서에 맞춰, 각 타순에 맞게 점수 처리를 해주고
아웃이 날 경우, 타순을 유지한 채로 다음 이닝으로 넘어가는 과정을 함수로 처리
'''
from itertools import permutations
import sys
input = sys.stdin.readline
N = int(input())

innings = [list(map(int, input().split())) for _ in range(N)]

result = 0  # 얻을 수 있는 최대 점수

# 현재 그라운드에 선수가 있는지 없는지 여부 체크
# 1루석에 있을 경우 ground[1] = 1 ...
# 점수를 획득할 경우, 각 점수별로 선수 이동 처리(끝에서 부터)
# 3루석에 선수 있는데 점수 획득시 1점 획득
# 0루석에 현재
'''
안타: 1 타자와 모든 주자가 한 루씩 진루한다.
2루타: 2 타자와 모든 주자가 두 루씩 진루한다.
3루타: 3 타자와 모든 주자가 세 루씩 진루한다.
홈런: 4 타자와 모든 주자가 홈까지 진루한다.
아웃: 0 모든 주자는 진루하지 못하고, 공격 팀에 아웃이 하나 증가한다
'''


def play_game(i, players):
    global result
    point = 0  # 획득한 점수
    # 마지막 이닝에 도다를때까지 게임 진행
    for curr_inning in innings:
        out = 0  # 현재 이닝에서 아웃의 수 카운팅
        # 현재 이닝에서의 그라운드의 상태
        g1, g2, g3 = 0, 0, 0
        # 현재 이닝에서 3아웃 전까지 수행한다.
        while out != 3:
            if curr_inning[players[i-1]-1] == 0:  # 아웃인 경우
                out += 1
            elif curr_inning[players[i-1]-1] == 1:  # 1루타
                point += g3  # 현재 g3에 선수가 있다면 점수 추가
                g1, g2, g3 = 1, g1, g2  # 선수들 한칸씩 이동
            elif curr_inning[players[i-1]-1] == 2:  # 2루타
                point += (g2+g3)  # g2와 g3에 있는 선수 수 만큼 점수 추가
                g1, g2, g3 = 0, 1, g1
            elif curr_inning[players[i-1]-1] == 3:  # 3루타
                point += (g1+g2+g3)  # g1~g3에 있는 선수 수 만큼 점수 추가
                g1, g2, g3 = 0, 0, 1
            else:  # 홈런
                point += (1+g1+g2+g3)
                g1, g2, g3 = 0, 0, 0
            i += 1
            i %= 9  # 범위 초과 방지
    # 최대 포인트 갱신
    result = max(result, point)


# 만들 수 있는 모든 게임 가짓수만큼 게임을 진행한다.
# 1번 타자의 위치는 고정되어 있으므로, 나머지 타자의 위치만 정하면 됨 => 8! 번에 대해 play_game연산 수행
# 1번을 제외한 나머지 가지수 만들어서 배열 만들기
players = [2, 3, 4, 5, 6, 7, 8, 9]

for selected in permutations(players, len(players)):
    selected = list(selected)
    # 4번째 자리에 1번 타자 고정시켜 선수 배열 생성
    selected_players = selected[:3] + [1] + selected[3:]
    # 해당 순번대로 게임 진행
    play_game(1, selected_players)

print(result)
