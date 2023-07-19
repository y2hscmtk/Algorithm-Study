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
    ground = [1, 0, 0, 0]
    out = 0  # 현재 이닝에서 아웃의 수 카운팅
    point = 0  # 획득한 점수
    curr = 0  # 현재 이닝 수
    # 마지막 이닝에 도다를때까지 게임 진행
    while curr < N:
        # 순번 정보를 토대로 게임을 진행한다.
        # 각 순번대로 이닝을 돌면서 각 순번에 맞는 점수 처리를 수행한다.
        for _ in range(9):
            if innings[curr][players[i-1]-1] == 0:  # 아웃인 경우
                out += 1
                if out == 3:  # 3아웃인지 체크
                    out = 0  # 0아웃으로 초기화
                    ground = [1, 0, 0, 0]  # 그라운드 초기화
                    curr += 1  # 다음 이닝으로 넘어가기
                    i += 1  # 다음 선수부터 시작
                    # start = i + 1  # 다음 이닝에서 게임을 시작할 타수의 번호
                    # i값 초기화x
                    break
                i += 1
                i %= 9
                continue  # 아웃인 경우는 이동 무시
            # 아웃이 아닌경우는 타수별로 선수들 이동
            for j in range(3, -1, -1):
                # 현재 자리에 선수가 있고, 이동했을때 4이상의 값이 된다면 +1
                if ground[j] == 1:  # 선수가 있다면
                    if j != 0:
                        ground[j] = 0  # 선수 이동
                    # 이동했을때 4이상의 값이 되는지 확인
                    if j + innings[curr][players[i-1]-1] >= 4:
                        point += 1  # 1점 추가
                    else:  # 4 이상의 값이 아니라면(영역 안에서 이동한다면)
                        # 해당 위치로 선수 이동
                        ground[j+innings[curr][players[i-1]-1]] = 1
            i += 1
            i %= 9  # 범위 초과 방지
        # 9번째 선수까지 문제없이 끝났다면

        # for i in range(start, len(players)):

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
