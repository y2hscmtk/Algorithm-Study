# https://www.acmicpc.net/problem/18428
'''
맵을 돌면서 빈 영역 'X'를 만나면, 장애물의 위치로 설정
장애물 3곳의 위치를 모두 정하기 전까지 재귀 호출
3곳의 위치를 모두 정했다면 감시를 피할수 있는지 테스트
감시를 피할 수 있다면 "YES" 출력 후 프로그램 종료
감시를 피할 수 없다면 백트래킹으로 현재 위치를 다시 빈 영역으로 바꾸고, 이어서 다른 영역을 변경해가면서 테스트
브루트포스가 끝난 후에도 "YES"가 한번도 나오지 않았다면 "NO" 출력후 프로그램 종료
'''
import sys
N = int(input()) # N x N 크기의 복도
# 현재 복도 상태 입력받기
corridor = [list(input().split()) for _ in range(N)]
# 해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다.
# 전체 선생님의 수는 5이하의 자연수, 전체 학생의 수는 30이하의 자연수이며 항상 빈 칸의 개수는 3개 이상으로 주어진다.

# 선생님 위치 파악 => 각 선생님의 위치에서 탐색을 시작할 것이기 때문
teacher = []
for i in range(N):
    for j in range(N):
        if corridor[i][j] == 'T':
            teacher.append([i,j])


# 선생님은 상하좌우의 방향에 대해서, 벽으로 가로막히기 전까지 관찰가능
dx = [0,0,-1,1]
dy = [-1,1,0,0]


# 선생님의 관찰 과정에서 학생이 발견 되었는지 아닌지를 확인하는 함수
def find_student():
    
    # 각 선생님들의 위치에서 탐색 시작
    for i in range(len(teacher)):
        # 모든 방향에 대해서
        for d in range(4):
            x,y = teacher[i]
            # 해당 방향으로
            # 한쪽 끝에 도달할때까지 반복
            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                # 영역을 벗어났는지 확인 => 벗어나지 않은 경우에 대해서
                if 0<=nx<N and 0<=ny<N:
                    # 학생을 발견하였다면 True리턴 => 이미 학생을 발견하였으므로 다른 방향과 다른 선생님에 대한 탐색 불필요
                    if corridor[nx][ny] == 'S':
                        return True
                    # 장애물을 발견하였다면 해당 방향으로의 탐색 종료
                    elif corridor[nx][ny] == 'O':
                        break
                    # 위의 경우에 해당하지 않는다면 탐색 위치만 변경
                    x = nx
                    y = ny
                else: # 영역을 벗어났다면
                    break # 다음 방향에서 탐색 진행
    # 모든 선생님의 탐색 결과, 학생이 발견되지 않았다면
    return False


# 장애물 3곳 설정하는 함수
def set_obstacle(count):
    # 만약 장애물을 3곳 다 선택하였다면 선생님의 탐색 시작
    if count == 3:
        if find_student():
            return
        else: # 학생을 찾지 못하였다 => 성공적으로 장애물을 설치함
            print("YES")
            sys.exit(0)
    
    # 아직 장애물을 3곳 다 선택하지 못했다면, 장애물 설치 작업 시작
    for i in range(N):
        for j in range(N):
            # 빈 영역 발견시, 장애물 설치
            if corridor[i][j] == 'X':
                corridor[i][j] = 'O' # 장애물 설치
                set_obstacle(count+1) # 장애물을 한개 추가로 설치했다는 의미로 +1
                corridor[i][j] = 'X' # 백트래킹

set_obstacle(0) # 장애물 설치 작업을 수행 => 장애물 다 설치되면 알아서 선생님 탐색 수행
# 프로그램이 아직 종료되지 않았다 => 학생이 기어코 발견되었다.
print("NO")
